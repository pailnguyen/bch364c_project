---
layout: page
title: Methods
permalink: /methods/
---

# Methods
**Summary**
Software: TensorFlow 1.1.0, Python 3.5.2, Microsoft Windows 10 Version 1607 (OS Build 14393.693)
Dataset: http://locate.imb.uq.edu.au/downloads.shtml (Organelle Image Collection - HeLa)
We only used the “Endogenous” data
Project and thresholding algorithm inspired by/implemented from: https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-110 (“Fast automated cell phenotype image classification” by Hamilton et al.)

Architecture: Convolution, ReLU, Max Pool, Normalization, Convolution, ReLU, Normalization, Max Pool, FCL, FCL, Softmax Loss Function

To start, we based our CNN off of an example CNN from Google for classifying images in the [CIFAR-10](http://www.cs.toronto.edu/~kriz/cifar.html) dataset, which contains 60000 32x32 images each belonging to one of ten specific classes (for example, “airplane”, “cat”, “frog”, etc.) Of course, it would be naive to simply feed microscopy images directly into this network; to do so would be to not take advantage of the specific characteristics of our data.
The first optimization we made arose from our observation that our images were grayscale rather than RGB. This means that the “luminance” value for each pixel of a microscopy image can take on a single integer value anywhere between 0 (black) and 255 (white), rather than a 3-tuple (R, G, B) where each of R, G, and B can independently take on an integer value between 0 and 255. By reducing the dimensionality of certain tensors from 3 to 1, we sped up the time it took to train the network over 10000 iterations.
Another optimization we made was to increase the size of images that the network saw during training. The CIFAR-10 classification network only looked at low-resolution 24x24 samples of 32x32 images. It was able to achieve >80% accuracy, largely due to the fact that enough variation between pixels remains to observe defining features of the ten image classes. In our case, we use 64x64 samples of 96x64 microscopy images (downscaled from the original 768x512 image by a factor of 4). Though this increased the time it took to train the network (to approximately 3 hours), it allowed us to surpass initial results of <50% classification accuracy.
In order to allow for variation between microscopy images, we additionally incorporated a step in training that would randomly rotate input images by a multiple of 90 degrees. We also added a step that would randomly vertically flip ~50% of incoming input images. This was in addition to the existing random horizontal flip step included in the CIFAR-10 network program.
To observe the images being processed by the network, as well as visually verify our intended network architecture, we used [TensorBoard](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tensorboard).
