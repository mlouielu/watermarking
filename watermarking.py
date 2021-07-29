# -*- coding: utf-8 -*-
import random

import click
from PIL import Image, ImageFont, ImageDraw


@click.command()
@click.argument("filename")
@click.argument("watermark_text")
@click.argument("outfile")
@click.option(
    "--row-density", default=6, type=int, help="Row density of the watermark text"
)
@click.option(
    "--col-density", default=8, type=int, help="Col density of the watermark text"
)
@click.option("--rotate", default=25, type=int, help="Rotate text by degree")
@click.option("--font-size", default=24, type=int, help="Watermark text font size")
def watermarking(
    filename: str,
    watermark_text: str,
    outfile: str,
    row_density: int = 6,
    col_density: int = 8,
    rotate: int = 25,
    font_size: int = 24,
):
    """Watermarking FILENAME image with WATERMARK_TEXT."""
    im = Image.open(filename).convert("RGBA")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("NotoSerifCJK-Bold.ttc", size=font_size)

    # Text
    text_im = Image.new("RGBA", font.getsize(watermark_text), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_im)
    text_draw.text((0, 0), watermark_text, (255, 255, 255, 129), font=font)

    # Rotate
    rotate_im = text_im.rotate(rotate, expand=True)

    # Watermark & Composite
    for col in range(-im.size[0] // 2, im.size[0], im.size[0] // col_density):
        for row in range(-im.size[1] // 2, im.size[1], im.size[1] // row_density):
            watermark_im = Image.new("RGBA", im.size, (255, 255, 255, 0))
            watermark_im.paste(
                rotate_im,
                (col + random.randrange(-80, 80), row + random.randrange(-40, 40)),
            )
            im = Image.alpha_composite(im, watermark_im)

    im.save(outfile)


if __name__ == "__main__":
    watermarking()
