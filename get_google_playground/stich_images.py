import concurrent.futures
import os
from collections import namedtuple

import cairosvg
import requests
from PIL import Image

ImageData = namedtuple(
    typename="ImageData",
    field_names=["image", "row", "col"],
)


def download_image(
    base_url: str,
    row: int,
    col: int,
    download_dir: str,
) -> None:
    file_path = create_svg_file_path(
        download_dir=download_dir,
        row=row,
        col=col,
    )

    if not os.path.exists(
        path=file_path,
    ):
        url = f"{base_url}/{row:02d}_{col:02d}.svg"
        print(f"Downloading {url}")
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, "wb") as svg_file:
                svg_file.write(response.content)
        else:
            print(f"Failed to download {url}")


def download_images(
    base_url: str,
    rows: int,
    columns: int,
    download_dir: str,
) -> None:
    if not os.path.exists(
        path=download_dir,
    ):
        os.makedirs(
            name=download_dir,
        )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for row in range(rows):
            for col in range(columns):
                executor.submit(
                    download_image,
                    base_url,
                    row,
                    col,
                    download_dir,
                )


def stitch_images(
    download_dir: str,
    rows: int,
    columns: int,
    output_path: str,
) -> None:
    images_data = svg_to_png(
        download_dir=download_dir,
        columns=columns,
        rows=rows,
    )

    images_data.sort(
        key=lambda image_data: (image_data.row, image_data.col),
    )

    image_width = max(image.width for image, _, _ in images_data)
    image_height = max(image.height for image, _, _ in images_data)
    final_width = image_width * columns
    final_height = image_height * rows

    final_image = Image.new(
        "RGB",
        (final_width, final_height),
    )
    for image, row, col in images_data:
        x = col * image_width
        y = row * image_height
        final_image.paste(
            im=image,
            box=(x, y),
        )

    final_image.save(output_path)


def svg_to_png(
    download_dir: str,
    columns: int,
    rows: int,
) -> list[ImageData]:
    images: list[ImageData] = []

    for row in range(rows):
        for col in range(columns):
            print(f"Converting {row:02d}_{col:02d}.svg to PNG")
            try:
                image = convert_svg_to_png(
                    create_svg_file_path(
                        download_dir=download_dir,
                        row=row,
                        col=col,
                    ),
                )
            except Exception as exc:
                print(f"Generated an exception: {exc}")
            else:
                images.append(
                    ImageData(image, row, col),
                )

    return images


def create_future_to_image_dict(
    executor: concurrent.futures.ThreadPoolExecutor,
    rows: int,
    columns: int,
    download_dir: str,
) -> dict[concurrent.futures.Future, tuple[int, int]]:
    future_to_image = {
        executor.submit(
            convert_svg_to_png,
            create_svg_file_path(
                download_dir=download_dir,
                row=row,
                col=col,
            ),
        ): (row, col)
        for row in range(rows)
        for col in range(columns)
    }

    return future_to_image


def convert_svg_to_png(
    file_path: str,
) -> Image.Image:
    try:
        if os.path.exists(
            file_path,
        ):
            png_file_path = file_path.replace(".svg", ".png")
            cairosvg.svg2png(
                url=file_path,
                write_to=png_file_path,
            )
            image = Image.open(png_file_path)

            return image
        else:
            print(f"{file_path} does not exist")
    except Exception as e:
        print(f"An error occurred while converting {file_path} to PNG: {e}")


def create_svg_file_path(
    download_dir: str,
    row: int,
    col: int,
) -> str:
    return os.path.join(download_dir, f"{row:02d}_{col:02d}.svg")


def main() -> None:
    url = "https://searchplayground.google/static/tiles/vector/3"
    rows = 4
    columns = 8
    download_dir = "downloaded_images"
    output_path = "output_image.png"

    print(f"Downloading images from {url} to {download_dir}")
    download_images(
        base_url=url,
        rows=rows,
        columns=columns,
        download_dir=download_dir,
    )

    print(f"Stitching images into {output_path}")
    stitch_images(
        download_dir=download_dir,
        rows=rows,
        columns=columns,
        output_path=output_path,
    )


if __name__ == "__main__":
    main()
