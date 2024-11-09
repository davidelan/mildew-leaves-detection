![Banner](https://github.com/davidelan/mildew-leaves-detection/blob/main/images/cherry_leaves.jpg)


## Table of Contents
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and validation](#hypothesis-and-validation)
4. [Rationale for the model](#the-rationale-for-the-model)
5. [Trial and error](#trial-and-error)
6. [Implementation of the Business Requirements](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
7. [Machine Learning Business case](#machine-learning-business-case)
8. [Dashboard design](#dashboard-design-streamlit-app-user-interface)
9. [CRISP DM Process](#the-process-of-cross-industry-standard-process-for-data-mining)
10. [Bugs](#bugs)
11. [Deployment](#deployment)
12. [Technologies used](#technologies-used)
13. [Credits](#credits)

### Deployed version at [cherry-powdery-mildew-detector.herokuapp.com](https:)

## Dataset Content

4,208 images of individual cherry leaves set against a neutral background constitute the dataset used for this project. 
The dataset contains photos that were taken in a crop fields of the client. The field featured leaves that are either healthy or affected by a biotrophic fungus commonly known as **powdery mildew**. 
The dataset van be found on [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).

## Business Requirements

Our client, Farmy & Foods, a company in the agricultural sector, approached us to create a machine learning-based system that can quickly identify whether a cherry tree is infected with powdery mildew and requires fungicide treatment.

The system is designed to analyze images of cherry leaves and instantly determine if the tree is healthy or in need of attention. This request came as part of the company’s goal to automate the current manual inspection process. Farmy & Foods operates thousands of cherry trees across multiple farms nationwide, making the manual approach impractical and inefficient due to the time it takes to assess each tree individually.

Summarizing:

1. The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
3. The client is interested in obtaining a prediction report of the examined leaves. 

## Hypothesis and validation

**Hypothesis**: Infected cherry leaves exhibit distinct markings that set them apart from healthy ones.
   - __How to validate__: Create an average image study that can help to investigate the disease and its implications.<br/>

### Hypothesis 1
> Infected cherry leaves exhibit distinct markings that set them apart from healthy ones.

**1. Introduction**

### Distinctive Features of Infected Leaves

 The hypothesis is that infected leaves show dinstinct characteristics, which give space for a consistent differentiation. Specifically, coloration patterns and textures in the images are a very suitable candidate for Convolutional Neural Network (CNN) model investigation.