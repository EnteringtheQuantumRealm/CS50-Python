"""
CS50 P-Shirt

In a file called shirt.py, implement a program that expects exactly two command-line arguments:
 - in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
 - in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input
after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt with Image.paste,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and
save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
"""

from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        inpimg = os.path.splitext(sys.argv[1])
        outimg = os.path.splitext(sys.argv[2])
        if outimg[1].lower() not in format:
            sys.exit("Invalid output")
        elif inpimg[1].lower() != outimg[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            wearing_shirt(sys.argv[1], sys.argv[2])


def wearing_shirt(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_resized = ImageOps.fit(input, shirt.size)
            input_resized.paste(shirt, mask = shirt)
            input_resized.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()