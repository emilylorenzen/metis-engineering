Emily Lorenzen

Metis Bootcamp - Engineering

8/11/2021

# Project Proposal 


## Question/Need
Phenomics is an emerging field within the biomedical sciences that studies phenotypes on with the integration of many features. Traditionally, phenomics relied mostly on genomic data, due to the experimental ease and rapidly declining costs of genotyping. However, there are other methods that can also provide insight into phenotypes. One of these methods is cellular imaging, which, like genomics, results in high dimensionality data. In this project, I will analyze the images of immune cells taken after exposure to an immunological agent. 

## Data

Data will be downloaded from RxRx.ai, a depository of publicly shared data produced by the company Recursion. I will be analyzing Rxrx2, a dataset resulting from cell imaging experiment on HUVEC cells exposed to immunological perturbants. The data set consists of a total of ~800,0000 images. Each are 1024 x 1024 pixels, are represent one 6 channel of a complete picture. Therefore, a single picture will have the dimensions of 1024 x 1024 x 6.

A single unit of data will be the six images, immunological perturbant, and mechanism of action. My target will be MoA of the immunological agent. 

## Tools

Google Cloud will be used to store data and GCP will be used for cloud computing.

Keras will be used to build convolutional neural networks. Sklearn will be used for model evaluation. 

Streamlit will be used to create an interactive interface that allows other researchers to upload their own data. 

## Minimum Viable Project:

For a minimum viable project I will focus on building a neural network model for a subset of the data (about 1/24th).

