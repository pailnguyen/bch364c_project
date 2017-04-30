---
layout: page
title: Methods
permalink: /methods/
---

**Summary**

Software: TensorFlow 1.1.0 (`pip3 install tensorflow`), [Python 3.5.2](https://www.python.org/downloads/), Microsoft Windows 10 Version 1607 (OS Build 14393.693) (also tested on macOS Sierra)

Dataset: [http://locate.imb.uq.edu.au/downloads.shtml](http://locate.imb.uq.edu.au/downloads.shtml) (Organelle Image Collection - HeLa)

* We only used the “Endogenous” portion of the dataset.

Project and thresholding algorithm inspired by/implemented based on [“Fast automated cell phenotype image classification” by Hamilton et al.](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-110).

Architecture: Convolution, ReLU, Max Pooling, Normalization, Convolution, ReLU, Normalization, Max Pooling, Fully-Connected (FC), FC, Softmax Loss

The convolution layer uses a filter (a feature matrix) to detect features in the image. This layer “scrolls” through the image by a specified stride length, computing the dot product of the matrix to the input, and returns a feature map. Increasing the depth of a convolution layer increases the number of features that the layer detects. The convolution operator is a linear operator, so nonlinearity must be introduced back into the CNN to account for nonlinear data (most data). This is done by a ReLU (rectified linear unit) operation that changes all negative values to 0 while preserving positive values. This is a computationally efficient way to accelerate network training by avoiding the problem of having a near-0 gradient (which would greatly slow down any learning).

![Example of ReLU function being applied to a feature map from https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-07-at-6-18-19-pm.png)

**Figure 1.** Example of ReLU function being applied to feature map (image from https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)

Max pooling can be done after convolution layers to reduce dimensionality of the feature map while preserving the important information. The image is divided into small “windows” and a max value is preserved for each window. Spatial pooling reduces the size of the following inputs, thereby reducing computing power need. It also prevents overfitting of the data, allowing the trained machine to generalize results to new images.

![Visual depiction of max pooling from http://cs231n.github.io/convolutional-networks/.](http://cs231n.github.io/assets/cnn/maxpool.jpeg)

**Figure 2.** Visual depiction of max pooling (from http://cs231n.github.io/convolutional-networks/).

A normalization step scales all neurons to each other, preventing neurons from saturating if inputs are of different scales and increases generalizability of the results. These lower level layers have neurons that are only connected locally and extract feature information from small subsections of the image. The final layers are fully connected layers (FCLs). These layers have neurons that are all fully connected to each other with each connection and neuron having its own weight. Feeding the input from the convolution layers through these FCLs and results in a classification probability output. A softmax loss function calculates the deviation of these probabilities from training data.

The CNN is trained by a cycle of forward and backpropagation. In forward propagation, the image is used as input and is fed through the CNN from the lower level convolution layers to the higher level FCLs. This results in the output probabilities which are then compared to the real training data values to calculate error. In backpropagation, this error is fed back down through the CNN by means of a gradient descent. This gradient descent is used to adjust the weights of each connection proportional to their contributions towards the error. This process is continually cycled to adjust connection weights, lowering error to approach a minimum error. The training can be cycled until a designated stop point, usually a certain number of cycles before the error reaches a plateau.

**Training Workflow**
* `batch_resize.py` was written to create downscaled copies of the endogenous microscopy images.
* `generate_image_bytes.py` was written to compact and couple image labels with image luminance data
* In short, labels are represented with one byte; this is followed by a flattened bytestring representation of the associated image. This script partitioned data into files (`training_batch.bin` and `test_batch.bin`).
* `generate_threshold_image_bytes.py` was written to replicate Hamilton *et al.*’s thresholding method. We found that feeding our network threshold images lowered the final accuracy of our network, likely due to reduced luminance information (as threshold image pixels are solely either black or white).
* `jkl_train.py` was run to train our model according to the model specification programmed in `jkl.py`. `jkl_eval.py` provided accuracy as the number of correct predictions divided by the total number of test images evaluated.

To start, we based our CNN off of an example CNN from Google for classifying images in the [CIFAR-10](http://www.cs.toronto.edu/~kriz/cifar.html) dataset, which contains 60000 32x32 images each belonging to one of ten specific classes (for example, “airplane”, “cat”, “frog”, etc.) Of course, it would be naive to simply feed microscopy images directly into this network; to do so would be to not take advantage of the specific characteristics of our data.
The first optimization we made arose from our observation that our images were grayscale rather than RGB. This means that the “luminance” value for each pixel of a microscopy image can take on a single integer value anywhere between 0 (black) and 255 (white), rather than a 3-tuple (R, G, B) where each of R, G, and B can independently take on an integer value between 0 and 255. By reducing the dimensionality of certain tensors from 3 to 1, we sped up the time it took to train the network over 10000 iterations.
Another optimization we made was to increase the size of images that the network saw during training. The CIFAR-10 classification network only looked at low-resolution 24x24 samples of 32x32 images. It was able to achieve >80% accuracy, largely due to the fact that enough variation between pixels remains to observe defining features of the ten image classes. In our case, we use 64x64 samples of 96x64 microscopy images (downscaled from the original 768x512 image by a factor of 8). Though this increased the time it took to train the network (to approximately 5 hours), it allowed us to surpass initial results of <50% classification accuracy.
In order to allow for variation between microscopy images, we additionally incorporated a step in training that would randomly rotate input images by a multiple of 90 degrees. We also added a step that would randomly vertically flip ~50% of incoming input images. This was in addition to the existing random horizontal flip step included in the CIFAR-10 network program. The learning rate of our network gradually decreased over time to lower the chances of “overshooting” and skipping over local minima in the loss function landscape.
To observe the images being processed by the network, as well as visually verify our intended network architecture, we used [TensorBoard](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tensorboard).

We reimplemented Hamilton et al.’s thresholding method (based on their written description in the paper) and fed our thresholded images (see image below) as alternate inputs to our network. We found that we were only able to achieve ~80% accuracy and suspect that this is due to not having complete luminance information available to the CNN for feature extraction. It is unclear whether counting the number of neighboring white pixels for each pixel of the thresholded images, then feeding those 2D sets of counts as pseudo-images to the network (with “luminance” values ranging from 0 to 8), would result in better classification, but we suspect that this may not be the case. For one, Hamilton *et al.* ultimately aggregated their counts into 3 sets of 9 threshold adjacency statistics to generate 27 statistics per image.

![Comparison of downscaled original and thresholded images.](http://i.imgur.com/x9TtAZp.png)

**Figure 3.** Comparison of downscaled original and thresholded images. Note that the images seen by the network were 96x64 in size; they are scaled up here (using nearest-neighbor scaling) for visual clarity.
