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

 We hypothesize that cherry leaves infected with powdery mildew exhibit unique visual characteristics that differentiate them from healthy leaves. These characteristics, including specific coloration patterns and textures, can be captured and analyzed by a CNN-based model, allowing it to effectively distinguish between healthy and infected leaves.

### Efficiency in Detection

   The machine learning program is expected to significantly accelerate the cherry leaf examination process. By automating the detection of powdery mildew, the model can save substantial amounts of time, effort, and money compared to manual inspection. With an anticipated accuracy of about 99%, the model could reduce the time and resources required for inspections by at least 90%.

### Reduction of Human Error

   Manual inspections of cherry leaves are prone to human errors, such as overlooking early signs of infection. The model is designed to minimize these errors by consistently applying the same detection criteria, leading to more reliable and accurate results. This could be particularly valuable in large-scale operations where the volume of leaves to be inspected is high.

### Early Detection and Prevention

   Detecting powdery mildew at an early stage is crucial for preventing the spread of the disease to a large number of trees. The model is hypothesized to be more effective than human inspectors at identifying the early signs of infection, thus enabling timely intervention. This early detection could lead to more effective treatment and management strategies, ultimately protecting crop yields and quality.

### Business Impact

   By integrating this machine learning program into their operations, agricultural businesses can improve their crop management practices. The ability to quickly and accurately identify infected leaves allows for faster response times, reducing the risk of widespread infection and potentially leading to significant cost savings.

**2. Observation**

An Image Montage shows the evident difference between a healthy leaf and an infected one. 

![montage_healthy](https://github.com/cla-cif/Cherry-Powdery-Mildew-Detector/blob/main/readme_images/montage_healthy.png)
![montage_infected](https://github.com/cla-cif/Cherry-Powdery-Mildew-Detector/blob/main/readme_images/montage_infected.png)

Difference between average and variability images shows that affected leaves present more white stipes on the center.

![average variability between samples](https://github.com/cla-cif/Cherry-Powdery-Mildew-Detector/blob/main/readme_images/average_image.png)

While image difference between average infected and average infected leaves shows no intuitive difference. 

![average variability between samples](https://github.com/cla-cif/Cherry-Powdery-Mildew-Detector/blob/main/readme_images/avg_diff.png)

**3. Conclusion**

The model was able to detect such differences and learn how to differentiate and generalize in order to make accurate predictions.
A good model trains its ability to predict classes on a batch of data without adhering too closely to that set of data.
In this way the model is able to generalize and predict future observation reliably because it didn't 'memorize' the relationships between features and labels as seen in the training dataset but the general pattern from feature to labels.