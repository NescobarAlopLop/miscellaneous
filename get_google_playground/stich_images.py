import os

import cairosvg
import requests
from PIL import Image


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
    images = svg_to_png(columns, download_dir, rows)

    images.sort(key=lambda x: (x[1], x[2]))

    image_width = max(image.width for image, _, _ in images)
    image_height = max(image.height for image, _, _ in images)
    final_width = image_width * columns
    final_height = image_height * rows

    final_image = Image.new("RGB", (final_width, final_height))

    for image, row, col in images:
        x = col * image_width
        y = row * image_height
        final_image.paste(image, (x, y))

    final_image.save(output_path)


def svg_to_png(columns, download_dir, rows):
    images = []
    for row in range(rows):
        for col in range(columns):
            file_path = os.path.join(download_dir, f"{row:02d}_{col:02d}.svg")
            if os.path.exists(file_path):
                png_file_path = file_path.replace('.svg', '.png')
                cairosvg.svg2png(url=file_path, write_to=png_file_path)
                image = Image.open(png_file_path)
                images.append((image, row, col))

    return images


if __name__ == "__main__":
    url = "https://searchplayground.google/static/tiles/vector/3"
    rows = 4
    columns = 8
    download_dir = "downloaded_images"
    output_path = "output_image.png"

    download_images(url, rows, columns, download_dir)
    stitch_images(download_dir, rows, columns, output_path)
