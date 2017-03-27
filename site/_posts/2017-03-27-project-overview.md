---
layout: post
title: Project Overview
---
*by Steven Tran and Paul Nguyen*

{% marginnote margin1 %}
These authors contributed equally.
{% endmarginnote %}

{% blockquote Nelson and Cox, Lehninger Principles of Biochemistry %}
Proteins mediate virtually every process that takes place in a cell, exhibiting an almost endless diversity of functions. To explore the molecular mechanism of a biological process, a biochemist almost inevitably studies one or more proteins.
{% endblockquote %}

Protein structure determination is an important gateway step in many fields of research, from drug design to understanding protein function. Currently, structure determination is done using X-ray crystallography which requires tedious experimentation to obtain protein crystals suitable for X-ray diffraction. Reliable protein structure prediction could supplement crystallography to more easily determine protein structure. Unfortunately, structure prediction is still an unsolved problem. Protein structure prediction remains an important problem in bioinformatics. The most successful structure prediction software predominantly uses homology modeling and protein threading. De novo prediction is less successful due to limited understanding of protein folding dynamics. There have been few attempts to apply machine learning to structure prediction without reliance on sequence similarity in homologous proteins or secondary structure.

Here, we propose taking a supervised learning approach to this problem using an artificial neural network (ANN) in which input is derived from a training dataset constructed from known protein primary sequences and secondary structures parsed from several thousand PDB files. This ANN will use [TensorFlow][tf], an emerging machine learning platform that has not yet been applied to many biological datasets. We plan to use an architecture containing convolutional layers in order to simplify processing compared to using only layers in which all neurons are fully-connected. The accuracy of our network will be measured through validation with data not included in the training set. This project will potentially make use of [TACC][tacc] facilities to allow for greater amounts of data to be processed as well as for additional cycles of weight optimization. Ultimately, we hope to contribute to the existing literature in the field of machine learning for protein structure prediction with a novel procedure of comparable accuracy and/or efficiency to previously explored methods that are non-reliant on homology information.

Visit the links in the navigation bar to learn more.

[tf]: https://www.tensorflow.org/
[tacc]: https://www.tacc.utexas.edu/
