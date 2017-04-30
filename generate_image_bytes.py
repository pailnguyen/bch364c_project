# Copyright 2017 Paul Nguyen, Steven Tran.
# ==============================================================================

"""A script for generating data formatted similarly to the CIFAR-10 dataset.
   Takes a text file as an argument containing whitespace-separated pairs of
   cellular localization class and organelle feature reference.
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

with open(sys.argv[1], "r") as f:
  count = 0
  for line in f:
    count += 1
    (location, name) = line.strip().split()
    print(location, name)
    image_path = "./SubCellLoc/Endogenous/" + name + "_myc.png"
    image = Image.open(image_path)
    luminances = bytes(list(image.getdata()))
    if location not in locations:
      print("Unexpected location ({}) for {}".format(location, name))
    else:
      record_bytes = locations.index(location).to_bytes(
          1, sys.byteorder) + luminances

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
