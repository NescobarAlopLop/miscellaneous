# SVG to PNG Image Stitcher

This is short script to nick the Googles Puzzle picture.

The script uses the `httpx` library for downloading SVG images, `cairosvg` for converting SVG to PNG, and `PIL` for stitching the images together and saving the final image.

## Resulting Image

Here is an example of a resulting image:

![Resulting Image](https://github.com/NescobarAlopLop/miscellaneous/blob/master/get_google_playground/output_image.png)

Note: Replace `output_image.png` with the actual path to your output image.

You can install these dependencies using pip:

```bash
pip install httpx cairosvg pillow
```

```bash
python stitch_images.py
```

[Link](https://campushaifaac-my.sharepoint.com/:i:/g/personal/gkesaev_campus_haifa_ac_il/EUNjTMovWyRKsxlFodw6wSABcS5XEBGGCjByEPPy7qApUw?e=dZ7dIh) to a 4k image of the puzzle.
