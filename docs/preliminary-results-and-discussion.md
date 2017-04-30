---
layout: page
title: Results and Discussion
permalink: /results-and-discussion/
---

After several cycles of architecture modification and testing, we ended up with a CNN with a peak accuracy of 93.1%. Below is a graph from TensorBoard of how cross-entropy changed during training.

![](http://i.imgur.com/OQYEqvu.png)

**Figure 1.** Cross-entropy over time during CNN training. We used `tf.nn.sparse_softmax_cross_entropy_with_logits()`, which, as stated by the documentation, “measures the probability error in discrete classification tasks in which the classes are mutually exclusive”. After ~5 hours of training, cross-entropy dropped to 0.01435. Intuitively, a decrease in cross-entropy is an indication that neurons in the network are no longer making large mistakes in producing desired outputs (see [*Neural Networks and Deep Learning*](http://neuralnetworksanddeeplearning.com) by Michael Nielsen for more information).

![](http://i.imgur.com/2ue0aJ1.png)

**Figure 2.** Accuracy vs training steps. Accuracy was determined by an evaluation script that tested the CNN against test data separated from the dataset prior to training. Evaluation was run simultaneously to training and returned accuracy as the machine was being trained. Note the stepwise function of accuracy. The most likely cause of this step is that the machine learning happens in “chunks” where several iterations of weight adjustments suddenly results in the machine learning a certain image classification well.

There are several potential ways to improve our CNN’s accuracy. One idea would be to modify it to take in input images of varying dimensions. We could then crop images depending on the regions of non-black pixels visible in the image. This ensures that our image crops generated during training contain as much information as possible of the actual pixels corresponding to fluorescently-tagged protein expression.

Additionally, an easy way to increase training accuracy is to simply train longer; we trained for only up to 10000 steps due to using limited home computing resources and wanting to iterate quickly, but the original CIFAR-10 classification network we modeled our approach on used 1000000 steps (due to only having to process 24x24 crops and making use of high-powered [Nvidia Tesla K40m GPUs](https://en.wikipedia.org/wiki/Nvidia_Tesla)). It is interesting to note that although we use only 10000 steps, our training plateaued relatively early. This is likely due to the small dataset size. In order for increasing training steps to be useful, there must also be an increase in dataset size to increase the amount of information that can be gleaned from training.

In the future, we may wish to implement [stochastic gradient descent (SGD)](https://arxiv.org/pdf/1206.1106.pdf) to avoid the problem of having to manually test and refine the initial learning rate and its annealing.

Perhaps the most important and most effective way to improve network accuracy is simply to feed a sufficiently large training dataset to the network. In the same way that a small sample size has a higher likelihood of being skewed from the population, having a small dataset increases the chances that the data seen does not accurately represent all existing data. Such skewed training data would cause the algorithm to fit itself to a deviant from the real world entity. Intuitively, we would expect that larger training datasets would allow the network to recognize more distinct features among different image classes as training progresses.

Lastly, it is possible that transfer learning could be applied to allow networks pre-trained on a general image classification task to be used for our specialized problem. Transfer learning could save time and computational resources while still possibly delivering acceptable accuracy. We are excited to see how machine learning, and deep learning in particular, will continue to change the field of bioinformatics, and we hope to apply similar deep learning approaches to even larger datasets in the future.
