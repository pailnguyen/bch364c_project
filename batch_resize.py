# Copyright 2017 Paul Nguyen, Steven Tran.
# ==============================================================================

"""A script for batch resizing (shrinking) organelle images.
   Takes a directory containing .tif images as an argument.
"""

from PIL import Image
import os
import sys

# images start off as 768x512
# downscale by 8x
final_image_size = (96, 64)

directory = sys.argv[1]

for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        try:
            image = Image.open(directory + "\\" + filename)
        except Exception as e:
            print("Problem opening {0}: {1}".format(filename, e))
            continue

        resized_image = image.resize(final_image_size, Image.NEAREST)
        path = directory + "\\" + os.path.splitext(filename)[0] + ".png"
        print(path)
        resized_image.save(path)
print("resizing complete")
