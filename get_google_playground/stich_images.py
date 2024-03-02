import concurrent.futures
import os
import threading
from collections import namedtuple

import cairosvg
import requests
from PIL import Image

lock = threading.Lock()

ImageData = namedtuple('ImageData', ['image', 'row', 'col'])


def download_images(base_url, rows, columns, download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    for row in range(rows):
        for col in range(columns):
            file_path = os.path.join(download_dir, f"{row:02d}_{col:02d}.svg")

            if not os.path.exists(file_path):
                url = f"{base_url}/{row:02d}_{col:02d}.svg"
                print(f"Downloading {url}")
                response = requests.get(url)
                if response.status_code == 200:
                    with open(file_path, "wb") as svg_file:
                        svg_file.write(response.content)
                else:
                    print(f"Failed to download {url}")


def stitch_images(download_dir, rows, columns, output_path):
    images_data = svg_to_png(columns, download_dir, rows)

    images_data.sort(key=lambda image_data: (image_data.row, image_data.col))

    image_width = max(image.width for image, _, _ in images_data)
    image_height = max(image.height for image, _, _ in images_data)
    final_width = image_width * columns
    final_height = image_height * rows

    final_image = Image.new("RGB", (final_width, final_height))
    for image, row, col in images_data:
        x = col * image_width
        y = row * image_height
        final_image.paste(image, (x, y))

    final_image.save(output_path)


def svg_to_png(columns, download_dir, rows) -> list[ImageData]:
    images: list[ImageData] = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_image = create_future_to_image_dict(executor, rows, columns, download_dir)
        for future in concurrent.futures.as_completed(future_to_image):
            row, col = future_to_image[future]
            try:
                image = future.result()
            except Exception as exc:
                print(f'Generated an exception: {exc}')
            else:
                images.append(ImageData(image, row, col))

    return images


def create_future_to_image_dict(executor, rows, columns, download_dir):
    future_to_image = {
        executor.submit(convert_svg_to_png, create_svg_file_path(download_dir, row, col)): (row, col)
        for row in range(rows) for col in range(columns)
    }

    return future_to_image


def convert_svg_to_png(file_path):
    try:
        if os.path.exists(file_path):
            png_file_path = file_path.replace('.svg', '.png')
            with lock:
                cairosvg.svg2png(url=file_path, write_to=png_file_path)
            image = Image.open(png_file_path)

            return image
    except Exception as e:
        print(f"An error occurred while converting {file_path} to PNG: {e}")


def create_svg_file_path(download_dir, row, col):
    return os.path.join(download_dir, f"{row:02d}_{col:02d}.svg")


def main():
    url = "https://searchplayground.google/static/tiles/vector/3"
    rows = 4
    columns = 8
    download_dir = "downloaded_images"
    output_path = "output_image.png"

    download_images(url, rows, columns, download_dir)
    stitch_images(download_dir, rows, columns, output_path)


if __name__ == "__main__":
    main()
