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

### Deployed version at [cherry-powdery-mildew-detector.herokuapp.com](https://mildew-leaves-detection-dav-9ff1fd9edf31.herokuapp.com/)

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

### Hypothesis
> Infected cherry leaves exhibit distinct markings that set them apart from healthy ones.

**1. Introduction**

### Features of Infected Leaves

 The hypothesis is that infected leaves show dinstinct characteristics, which give space for a consistent differentiation. Specifically, coloration patterns and textures in the images are a very suitable candidate for Convolutional Neural Network (CNN) model investigation.
 

### Efficiency

The machine learning system is designed to greatly speed up the process of cherry leaf analysis. By automating the identification of powdery mildew, the tool can save a significant amount of time, labor, and financial resources compared to traditional manual inspections. With an estimated very high accuracy rate, it is expected to cut down inspection time and resource use by up to 90%.

### Human Error

Human inspections of cherry leaves are often susceptible to mistakes, such as missing early indicators of disease. This model aims to reduce such errors by uniformly applying detection criteria, ensuring more consistent and precise outcomes. This feature is especially beneficial for large-scale operations with a high volume of leaves to examine.

###  Prevention and Early Detection

Identifying powdery mildew early is essential to stopping its spread across a large orchard. The model is thought to outperform human inspectors in spotting the initial signs of infection, enabling faster intervention. Early detection can lead to more effective treatment, better management practices, and ultimately safeguard both crop yield and quality.

### Financial Impact

Integrating this machine learning solution into agricultural practices offers businesses the chance to enhance their crop management strategies. The ability to quickly and accurately detect infected leaves allows for quicker action, lowering the risk of widespread disease and offering substantial potential for cost savings.

------------------------------------
--------- fino a qui ---------------

**2. Observation**

In the following emages you can appreciate the difference between cherry leaves that are healthy and cherry leaves that are affected by mildew desease:

![montage_healthy](https://github.com/davidelan/mildew-leaves-detection/blob/main/images/montage_healthy.png)
![montage_infected](https://github.com/davidelan/mildew-leaves-detection/blob/main/images/montage_mildew.png)


Here we can have a look and appreciate the slightly difference in the two leaves categories with respect to their average and variability: 

![average variability healthy](https://github.com/davidelan/mildew-leaves-detection/blob/main/outputs/v1/avg_var_healthy.png)
![average variability mildew](https://github.com/davidelan/mildew-leaves-detection/blob/main/outputs/v1/avg_var_powdery_mildew.png)

While image difference between average infected and average infected leaves shows no intuitive difference. 

It seems very difficult if not impossible to intuitively distinguish between images of healthy and infected leaves:

![average variability](https://github.com/davidelan/mildew-leaves-detection/blob/main/outputs/v1/avg_diff.png)

**3. Conclusion**

The model successfully identified these differences and learned to distinguish and generalize, enabling it to make precise predictions. A well-trained model develops its capacity to predict classes based on a data batch without overly relying on the specifics of that batch. By doing so, it can generalize effectively and make dependable predictions for future data, as it focuses on the overall patterns connecting features and labels, rather than simply memorizing the relationships within the training set.

---

