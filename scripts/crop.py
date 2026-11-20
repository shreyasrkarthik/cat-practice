#!/usr/bin/env python3
"""Crop a browser screenshot of a bare image (dark viewer background) to the image itself."""
import sys
from PIL import Image, ImageChops
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
bg = Image.new("RGB", im.size, im.getpixel((2, 2)))
diff = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 18 else 0)
box = diff.getbbox()
out = im.crop(box) if box else im
out.save(dst, optimize=True)
print(dst, out.size)
