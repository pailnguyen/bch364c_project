---
layout: page
title: Introduction and Background
permalink: /introduction/
---

Deep learning using convolutional neural networks (CNNs) is an increasing “trendy” field due to potential application to a [wide variety of domains](www.nature.com/nature/journal/v521/n7553/full/nature14539.html). In short, CNNs use layers of “neurons” and convolutional filters that process the input from these layers in order to detect broad features. The most popular use case for CNNs has been image classification, in which a program is tasked to assign classes to images based on the features detected within such images. CNNs that are adept at this task will limit the need for laborious manual image labeling. Automated image classification and object recognition have applications in face enhancement in photography, filtering of inappropriate content in search engine results, and, we believe, the problem Hamilton et al. tackled in 2007 of cell phenotype image classification.

![](http://www.nature.com/nature/journal/v521/n7553/images/nature14539-f2.jpg)

**Figure 1.** Image of a standard convolutional neural network architecture in action. Image taken from [LeCun *et al.*, 2015.](www.nature.com/nature/journal/v521/n7553/full/nature14539.html)

[Hamilton *et al.*](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-110) used threshold adjacency statistics to train a support vector machine (SVM) for cell organelle classification. This resulted in a fast and accurate method for determining locations that fluorescently-tagged proteins were being endogenously expressed in HeLa cells. In our work, we have developed a potential alternative to their thresholding technique by instead using downscaled versions of the fluorescent microscopy images as input for a convolutional neural network, rather than deriving threshold adjacency statistics from the images for training an SVM.

[TensorFlow](http://download.tensorflow.org/paper/whitepaper2015.pdf) is an open-source machine learning software library developed by Google for building and training neural networks. It has been successfully used in the past for written letter recognition and is used in this project for the purpose of classifying cell organelle images. Recent papers [have posited](http://www.cell.com/cell-systems/pdf/S2405-4712(16)00010-7.pdf) that the TensorFlow platform has untapped potential in biology. With this in mind, we decided to see how well a TensorFlow-backed CNN implementation (which we refer to as `jackal`) would perform at Hamilton’s classification task.
