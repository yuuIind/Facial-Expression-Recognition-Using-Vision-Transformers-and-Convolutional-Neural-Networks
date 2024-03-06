# Facial-Expression-Recognition-Using-Vision-Transformers-and-Convolutional-Neural-Networks
This repository contains the implementation and resources for a facial expression recognition system developed as a part of my graduation project at Yeditepe University. The project explores the use of efficient transformers models for vision tasks in the context of recognizing facial expressions from images.


## Abstract
Facial expression recognition (FER) is a subtask of emotion recognition that focuses on
categorizing human expressions from face images. It has numerous practical applications,
including security, advertising, healthcare, and recommendation systems. Recent
advancements in deep learning have led to significant progress in the field. This project tries
to find a lightweight and efficient method that combines convolutional neural networks
(CNNs) and transformers to achieve high performance for the FER task. The proposed
approach tries to improve on vision transformer on by combining a backbone network as a
feature extractor to obtain fine-level features from images. Various variants were tested on
the AffectNet database to find an effective approach, resulting in %55.54 accuracy on 8 class
with using only 5.67M parameters.


## RESEARCH OBJECTIVE
The goal of this project is to develop a lightweight and efficient method for facial expression
recognition (FER). The proposed approach aims to improve the performance of FER systems
by incorporating a backbone network into the vision transformer. The goal is to achieve high
performance while using fewer parameters, making the model more practical for real-world
applications. Specifically, the project aims to investigate the effectiveness of combining CNNs
and transformers for FER and evaluate different backbone networks as feature extractors. The
goal is to experiment with different architectures and training techniques to improve the
performance of the proposed method. The proposed method will be evaluated on the
AffectNet[1](https://arxiv.org/abs/1708.03985) database and compared to state-of-the-art approaches to analyse its strengths and
weaknesses.


## Project Overview
This project tries to find a lightweight and efficient method to achieve high performance for the FER task. It builds on the methods proposed by Hassani et al.[2](https://arxiv.org/abs/2104.05704). Backbone Network for extracting fine level features.Patch extractor is applied to extract relevant features from facial patches. Transformer encoder is implemented as described in [2](https://arxiv.org/abs/2104.05704). Training and Evaluation is conducted on AffectNet[1](https://arxiv.org/abs/1708.03985).


## Results

The proposed method achieves an accuracy of 55.54% on the 8-class facial expression recognition task using the AffectNet database, while utilizing only 5.67M parameters.

Top-1 test set accuracy comparisons. * variants trained without oversampling. For more, please, see [here](Reports/EE492_PROJECT%20REPORT_M.TASTAN_223SP.pdf)

| Model | Performance | #Params | link |
| --- | --- | --- | --- |
| VCCT-1 | 53.49% | 11.26M | [ckpt](/Models/Checkpoints/VCCT-1_ckpt_9.pt) |
| VCCT-2 | 53.41% | 11.71M | [ckpt](/Models/Checkpoints/VCCT-2_ckpt_10.pt) |
| *MCCT-1 | 48.19% | 3.00M | [ckpt](/Models/Checkpoints/MCCT-1_ckpt_20.pt) |
| MCCT-1 | 53.24% | 3.00M | [ckpt](/Models/Checkpoints/MCCT-1_ckpt_10.pt) |
| *MCCT-2 | 44.16% | 3.44M | [ckpt](/Models/Checkpoints/MCCT-2_ckpt_9.pt) |
| MCCT-2 | 54.19% | 3.44M | [ckpt](/Models/Checkpoints/MCCT-2_OS_ckpt_10.pt) |
| *MCCT-3 | 41.49% | 3.89M | [ckpt](/Models/Checkpoints/MCCT-3_ckpt_10.pt) |
| MCCT-3 | 51.21% | 3.89M | [ckpt](/Models/Checkpoints/MCCT-3_ckpt_10.pt) |
| *MCCT-6 | 45.26% | 5.23M | [ckpt](/Models/Checkpoints/MCCT-6_ckpt_10.pt) |
| MCCT-6 | 52.79% | 5.23M | [ckpt](/Models/Checkpoints/MCCT-6_OS_ckpt_10.pt) |
| *MCCT-7 | 40.79% | 5.67M | [ckpt](/Models/Checkpoints/MCCT-7_ckpt_9.pt) |
| MCCT-7 | 55.54% | 5.67M | [ckpt](/Models/Checkpoints/MCCT-7_OS_ckpt_10.pt) |

## Upcoming Updates
Currently only notebooks and some scripts are shared. A more structured model and training code will be released soon!

## License

This project is licensed under the MIT License.

<!--
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yuuIind/Facial-Expression-Recognition-Using-Vision-Transformers-and-Convolutional-Neural-Networks.git```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt```
3. -->
