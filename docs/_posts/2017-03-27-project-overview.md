---
layout: post
title: Abstract
---

*by Steven Tran and Paul Nguyen*

Accurate classification of microscopic imaging data is important for several reasons, including correct analysis of the functionality of specific proteins. In 2007, [Hamilton *et al.*](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-110) showed that a support vector machine (SVM) could be trained on threshold adjacency statistics derived from thresholded fluorescent microscopy images. Here we present an alternate approach that, rather than using thresholding, uses a basic convolutional neural network (CNN) trained directly on downscaled microscopy images to recognize characteristic features. Our goal was to take advantage of the luminance information in microscopy images that is lost upon thresholding. After training on images depicting the endogenous expression of fluorescently tagged proteins, we achieved a peak accuracy of 93.1%. This is comparable to, but unfortunately not greater than, the classification accuracy of 94.4% achieved by Hamilton *et al.*’s fast thresholding method, though we have several optimizations in mind that could improve the accuracy of future iterations of our CNN.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/IndianJackal.jpg/800px-IndianJackal.jpg)

Image taken from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:IndianJackal.jpg).

Visit the links in the navigation bar to learn more.
