# Copyright 2017 Paul Nguyen, Steven Tran.
# ==============================================================================

"""A script for generating data formatted similarly to the CIFAR-10 dataset.
   Takes a text file as an argument.
"""
from PIL import Image
import io
import os
import sys

# 11 total localization classes
# PM = plasma membrane
locations = ["Endosomes",
             "ER",
             "Golgi",
             "Lysosomes",
             "Mitochondria",
             "Nucleus",
             "PM",
             "Actin-Cytoskeleton",
             "Microtubule",
             "Peroxisomes"]
training_data = []
test_data = []


def threshold_image(image):
  (width, height) = image.size
  image_data = list(image.getdata())
  total_luminance = 0
  count = 0
  for luminance in image_data:
    if luminance > 30:
      total_luminance += luminance
      count += 1

  avg_luminance = total_luminance / count
  thresholded_image = image.copy()
  for i in range(1, width - 1):
    for j in range(1, height - 1):
      luminance = image.getpixel((i, j))
      if luminance > avg_luminance - 30 and luminance < avg_luminance + 30:
        thresholded_image.putpixel((i, j), 255)
      else:
        thresholded_image.putpixel((i, j), 0)

  return thresholded_image


with open(sys.argv[1], "r") as f:
  count = 0
  for line in f:
    count += 1
    (location, name) = line.strip().split()
    print(location, name)
    image_path = "./SubCellLoc/Endogenous/" + name + "_myc.png"
    image = Image.open(image_path)
    thresholded_image = threshold_image(image)
    threshold_image_path = "./SubCellLoc/Endogenous/" + name + "_threshold_myc.png"
    print("saving image to " + threshold_image_path)
    thresholded_image.save(threshold_image_path)

    if location not in locations:
      print("Unexpected location ({}) for {}".format(location, name))
    else:
      record_bytes = locations.index(location).to_bytes(
          1, sys.byteorder) + bytes(list(thresholded_image.getdata()))

      if count % 10 != 0:
        training_data.append(record_bytes)
      else:
        test_data.append(record_bytes)

  print("training data length: {}".format(len(training_data)))
  with open("/tmp/jkl_data/jkl_data/training_batch.bin", "bw") as train_file:
    train_file.write(b"".join(training_data))
    print("training data written")

  print("test data length: {}".format(len(test_data)))
  with open("/tmp/jkl_data/jkl_data/test_batch.bin", "bw") as test_file:
    test_file.write(b"".join(test_data))
    print("test data written")
