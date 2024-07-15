from PIL import Image, ImageDraw, ImageFont

import math

image = Image.open("bmw.jpg")
width, height = image.size
pix = image.load()

print(width, height)
