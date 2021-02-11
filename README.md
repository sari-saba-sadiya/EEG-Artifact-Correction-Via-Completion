# EEG-Artifact-Correction-Via-Completion

This is code for the artifact correction section of the paper "Unsupervised EEG Artifact Detection and Correction". Note that the feature extractor is an independent section that can be used with any artifact correction method (recently there have been quite a few including some notable example [1,2]).


[1] S. Phadikar, N. Sinha, and R. Ghosh, “Automatic eeg eyeblink artefactidentification  and  removal  technique  using  independent  componentanalysis  in  combination  with  support  vector  machines  and  denoisingautoencoder”

[2] B. Somers,  T.  Francart,  and  A.  Bertrand,  “A  generic  eeg  artifactremoval algorithm based on the multi-channel wiener filter.”

## Setup
The code here uses the [openbci 2a dataset](https://github.com/bregydoc/bcidatasetIV2a). Run `setup.py` from the folder to download the database. The data set used in the paper is too large for github and was instead [uploaded to the open science framework](https://osf.io/ednqx/), we recommend getting familiar with the code using the openbci2a dataset first. If you are interested in how the data was collected the following [repository contains all experimental procedure and code](https://github.com/sari-saba-sadiya/DEPV). 

First use `generate_hyperparam.ipynb` to create a hyper parameter file containing the topological space to be explored. Finally, the code `artifact_repair_autoencoder.ipynb` generates a NN to correct samples from a segment (Here of length T2=3) depending on the (T1=32 samples proceeding, and the T1=32 preceeding it), see function "create_repair_data" for a speciifc example.

Please open an issue or send an email to sadiyasa at msu for clarifications.

