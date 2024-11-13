![Banner](https://github.com/davidelan/mildew-leaves-detection/blob/main/images/cherry_leaves.jpg)


## Table of Contents
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and validation](#hypothesis-and-validation)
4. [Logic for the model](#logic-for-the-model)
5. [Trial and error](#trial-and-error)
6. [Mapping Business Requirements to Data Visualizations and ML Tasks](#mapping-business-requirements-to-data-visualizations-and-machine-learning-tasks)
7. [Machine Learning Business case](#machine-learning-business-case)
8. [Dashboard design](#dashboard-design)
9. [CRISP-DM Process](#crisp-dm-process)
10. [Manual Testing](manual-testing)
11. [Bugs](#bugs)
12. [Deployment](#deployment)
13. [Technologies used](#technologies-used)
14. [Credits](#credits)

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


**2. Observation**

In the following images you can appreciate the difference between cherry leaves that are healthy and cherry leaves that are affected by mildew desease:

![images-healthy](https://github.com/davidelan/mildew-leaves-detection/blob/main/images/images_healthy.png)
![images-infected](https://github.com/davidelan/mildew-leaves-detection/blob/main/images/images_mildew.png)


Here we can have a look and appreciate the slightly difference in the two leaves categories with respect to their average and variability: 

![average-variability-healthy](https://github.com/davidelan/mildew-leaves-detection/blob/main/outputs/v1/avg_var_healthy.png)
![average-variability-mildew](https://github.com/davidelan/mildew-leaves-detection/blob/main/outputs/v1/avg_var_powdery_mildew.png)


It seems very difficult if not impossible to intuitively distinguish between images of healthy and infected leaves:

![average-variability](https://github.com/davidelan/mildew-leaves-detection/blob/main/outputs/v1/avg_diff.png)

**3. Conclusion**

The model successfully identified these differences and learned to distinguish and generalize, enabling it to make precise predictions. A well-trained model develops its capacity to predict classes based on a data batch without overly relying on the specifics of that batch. By doing so, it can generalize effectively and make dependable predictions for future data, as it focuses on the overall patterns connecting features and labels, rather than simply memorizing the relationships within the training set.


---


## Logic for the model

 The model selected may not be the optimal one, but it was ultimately chosen after assessing the results of various tests and adjusting the model to meet the specific objective.

A strong model should minimize the computational resources it requires by simplifying the neural network architecture and reducing the number of trainable parameters, all while maintaining its ability to generalize, preserve accuracy, and reduce error.

An effective model enhances its ability to predict classes based on a dataset without overly fitting to that particular set. This allows the model to generalize, making it capable of reliably predicting future data since it doesn't simply memorize the relationships between features and labels in the training data, but instead learns the broader patterns that link features to labels.

The model is composed by 1 input layer, 3 hidden layers and 1 output layer.


## Mapping Business Requirements to Data Visualizations and Machine Learning Tasks

### Mapping First Business Requirement: Data Visualization
>The client needs a study which could allow a differentiation between healthy cherry leaves and cherry leaves affected by powdery mildew.

- As a user, I want to display the mean and standard deviation of images of healthy cherry leaves and of cherry leaves that contain powdery mildew so that I can optically distinguish between them.
- As a user, I want to display the difference between an average infected cherry leaf image and an average healthy cherry leaf image.
- As a user, I want to display an image montage for images of cherry leaves that are healthy and also of cherry leaves that contain powdery mildew.


### Mapping Second Business Requirement: Classification
>The client has the need to be able to fiugre out if a provided image of a cherry leaf is healthy or infected and see a report.

- As a user, I want to predict if a cherry leaf is healthy or contains powdery mildew.
- As a user, I want to upload cherry leaves images into the machine learning predicting program.
- As a user, I want to download the analysis report of each prediction.



### ### Mapping Third Business Requirement: Report
>The client is interested in obtaining a prediction report of the examined leaves. 

- As a client I want to obtain a report from the ML predictions on new leaves.  



## Machine Learning Business Case

### Current Status

Farmy and Foods currently depends on expensive trained staff to manually inspect cherry leaves and who can reliably identify healthy versus those infected with mildew. This process is not only time-consuming and labor-intensive but also susceptible to human error.

### Project Goal

The objective of this project is to create a ML model capable of accurately and efficiently categorizing cherry leaves as either "healthy" or "mildew-infected." Automating this task will help the business conserve valuable time, reduce labor, and optimize resources.

### Model Overview

This machine learning model is a supervised binary classification system that is trained using images of both healthy and mildew-infected cherry leaves. It learns to distinguish between the two categories by recognizing patterns in the images. The model then uses this knowledge to make a prediction, classifying the leaves as either "healthy" or "mildew."

### User Requirements

The customer needs an intuitive dashboard that allows them to easily upload both existing and new images of cherry leaves for analysis.

### Future Scope

Although the current emphasis is on cherry leaves, the model has the potential to be adapted for detecting diseases in other types of crops as well.

### Agile Process

This project was planned and executed using the Agile methodology. The work was divided into smaller, manageable user stories to facilitate a smooth and iterative development process. From the initial planning through to the final deployment, a structured yet flexible approach was adopted, allowing for adjustments at every stage.

To track progress and visualize the workflow, a [GitHub project board](https://github.com/users/davidelan/projects/4/views/1?layout=board) was set up using the Kanban board technique in Github. This method ensured efficient task management, with each project component being clearly outlined, prioritized, and completed in an orderly fashion.

![Kanban Board on Github](/images/agile_board.png)  



## Dashboard Design 
>Streamlit App User Interface

The dashboard is a visual application created with Streamlit, which allows the user to navigate through the following pages:

### Project Summary Page

This section gives an overview of the goal, dataset, phases and future improvements of the project.

![summary-page](/images/project_summary.png)


### Leaves Visualizer


- This part of the dashboard visually shows the two different categories of healthy and infected cherry leaves.

![sample-images](/images/sample_leaves.png)
---

- It is also possible for the user to visualize average and variability images of the two leaves' groups 

![difference-avr-variability](/images/difference-avr.png)
![difference-avr-variabilty-both](/images/difference-avr-both.png)
---

- The user can also choose to request an image montage of either healthy or infected leaves' images.

![montage-healthy](/images/montage_healthy.png)
![montage-infected](/images/montage_infected.png)
---


### Powdery mildew Detector

- In this part of the dashboard th euser can upload one or more cherry leaves images that can go through a live prediction.

![detector-upload](/images/prediction_1.png)
---

- The detector shows the image or images uploaded and formulates a prediction.

![detector-prediction](/images/prediction_2.png)
---


- The results of the prediction with the option to download the report is offered.

![detector-results](/images/prediction_3.png)


### Project Hypothesis
In this section of the dashboard various information about the project hypothesis and validation methods are displayed.
![hypothesis-page](/images/hypothesis.png)



### Machine Learning Performance
Visually user-friendly illustration of how the dataset was divided for the analysis, model training losses and accuracy and a generalised performance on test set.

- Data Distribution

![data-ditribution](/images/ml_performance.png)
---

- Model History

![training-history](/images/ml_history.png)
---

- Generalised Performance on Test Set

![sample-cherry-image-processed](/images/performance_test_set.png)
---


## CRISP-DM process
CRISP-DM, or Cross-Industry Standard Process for Data Mining, is a widely recognized framework designed to direct data mining projects.

- As a methodology, it outlines the common stages of a project, the tasks associated with each stage, and the connections between those tasks.
- As a process model, CRISP-DM offers a comprehensive view of the data mining life cycle.

### Business Understanding
The goal is to create a machine learning model that distinguishes between healthy and mildew-infected cherry leaves based on images. The model will offer real-time predictions via a dashboard, aiming for at least 97% accuracy to improve efficiency in manual inspections.

### Data Understanding
Collect images of healthy and infected cherry leaves, understanding the resolution, class distribution, and key features that differentiate them. Analyze the data for patterns and anomalies.

### Data Preparation
Label all images, remove non-image files, and standardize image sizes. Normalize pixel values and apply data augmentation to improve dataset diversity and model generalization.

### Modeling
Select a machine learning model, like a Convolutional Neural Network (CNN), for image classification. Train the model using the prepared data, experimenting with different architectures and hyperparameters for optimal performance.

### Evaluation
Assess the model's performance using accuracy, precision, recall, and F1-score. Ensure good performance across all classes, and cross-validate to prevent overfitting.

### Deployment
Deploy the model in a web app (e.g., using Streamlit) where users can upload images and get predictions. Monitor the model’s performance continuously and adjust as needed.


## Manual Testing

### Streamlit App
The Streamlit app was manually tested with the use of User Stories

#### Navigation

| Feature                           | Action        | Expected Result | Success |
| --------------------------------- | ------------- | --------------- | ------- |
| Project Summary                   | Click on link | Taken to page   | Yes     |
| Leaves Visualizer          | Click on link | Taken to page   | Yes     |
| Mildew Predictor          | Click on link | Taken to page   | Yes     |
| Project Hypothesis                | Click on link | Taken to page   | Yes     |
| Machine Learning Performance            | Click on link | Taken to page   | Yes     |

| Feature                     | Action                           | Expected Result                                                       | Success |
| --------------------------- | -------------------------------- | --------------------------------------------------------------------- | ------- |
| Cherry Leaves Visualizer    |                                  |                                                                       |         |
| Description of the page     | View Leaf Visualizer page        | Get descripting of the page aims                                      | Yes     |
| Samples Cherry Leaf Image   | Select the checkbox              | Open two sample images of healthy and mildew leaf                     | Yes     |
| Average and variability     | Select the checkbox              | Image with a note of difference between average and variability       | Yes     |
| Healthy and Powdery Mildew  | Select the checkbox              | Image with note of shows Differences between Healthy and Mildew       | Yes     |
| Image Montage               | Select the checkbox              | labels to select from Healthy or Mildew                               | Yes     |
| Create Montage              | Select the label                 | Montage of the images from the selected label                         | Yes     |



| Feature                                | Action                           | Expected Result                                                       | Success |
| -------------------------------------- | -------------------------------- | --------------------------------------------------------------------- | ------- |
| Leaf Mildew Detection page             |                                  |                                                                       |         |
| Page Objective                         | Leaf Mildew Detection page       |                                                                       | Yes     |
| Upload an Image                        | Click, or drag and drop          | Image Succesfuly upload                                               | Yes     |
| Make prediction                        | Click Make prediction            | See result and read the report                                        | Yes     |
| Download Report                        | Click Download Report            | Report download as a csv file                                         | Yes     |


| Feature                                | Action                           | Expected Result                                                       | Success |
| -------------------------------------- | -------------------------------- | --------------------------------------------------------------------- | ------- |
| Project Hypothesis page                |                                  |                                                                       |         |
| Read about the Project Hypothesis      | View Hypothesis Page             |  Project Hypothesis                                                   | Yes     |


| Feature                                | Action                           | Expected Result                                                       | Success |
| -------------------------------------- | -------------------------------- | --------------------------------------------------------------------- | ------- |
| ML Performance page                    |                                  |                                                                       |         |
| Technical details and performance metrics | View ML Performance Page      | Different visualizations of training history and evaluation metrics                                                 | Yes     |


### Automated Unit Tests
- There were no automated unit testing. It is planned for the future development.

[Back to top ⇧](#table-of-contents)



## Bugs

No known bugs to report.


## Deployment
The project is coded and hosted on GitHub and deployed with [Heroku](https://www.heroku.com/). 

### Creating the Heroku app 
The steps needed to deploy this projects are as follows:

1. Create a `requirement.txt` file in GitHub, for Heroku to read, listing the dependencies the program needs in order to run.
2. Set the `runtime.txt` Python version to a Heroku-20 stack currently supported version.
3. `push` the recent changes to GitHub and go to your [Heroku account page](https://id.heroku.com/login) to create and deploy the app running the project. 
3. Chose "CREATE NEW APP", give it a unique name, and select a geographical region. 
4. Add  `heroku/python` buildpack from the _Settings_ tab.
5. From the _Deploy_ tab, chose GitHub as deployment method, connect to GitHub and select the project's repository. 
6. Select the branch you want to deploy, then click Deploy Branch.
7. Click to "Enable Automatic Deploys " or chose to "Deploy Branch" from the _Manual Deploy_ section. 
8. Wait for the logs to run while the dependencies are installed and the app is being built.
9. The mock terminal is then ready and accessible from a link similar to `https://your-projects-name.herokuapp.com/`
10. If the slug size is too large then add large files not required for the app to the `.slugignore` file.
   
### Forking the Repository

- By forking this GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository. The steps to fork the repository are as follows:
    - Locate the [GitHub Repository](https://github.com/davidelan/mildew-leaves-detection) of this project and log into your GitHub account. 
    - Click on the "Fork" button, on the top right of the page, just above the "Settings". 
    - Decide where to fork the repository (your account for instance)
    - You now have a copy of the original repository in your GitHub account.



__You can find the live link to the site here: [Mildew leaves detection](https://mildew-leaves-detection-dav-9ff1fd9edf31.herokuapp.com/)__


## Technologies used

### Platforms
- [Heroku](https://en.wikipedia.org/wiki/Heroku) To deploy this project
- [Jupiter Notebook](https://jupyter.org/) to edit code for this project
- [Kaggle](https://www.kaggle.com/) to download datasets for this project
- [GitHub](https://github.com/): To store the project code after being pushed from Gitpod.
- [Gitpod](https://www.gitpod.io/) Gitpod Dashboard was used to write the code and its terminal to 'commit' to GitHub and 'push' to GitHub Pages.

### Languages
- [Python](https://www.python.org/)
- [Markdown](https://en.wikipedia.org/wiki/Markdown)
  
### Main Data Analysis and Machine Learning Libraries
<pre>
- tensorflow-cpu 2.6.0  used for creating the model
- numpy 1.19.2          used for converting to array 
- scikit-learn 0.24.2   used for evaluating the model
- streamlit 0.85.0      used for creating the dashboard
- pandas 1.1.2          used for creating/saving as dataframe
- matplotlib 3.3.1      used for plotting the sets' distribution
- keras 2.6.0           used for setting model's hyperparamters
- plotly 5.12.0         used for plotting the model's learning curve 
- seaborn 0.11.0        used for plotting the model's confusion matrix
- streamlit             used for creating and sharing this project's interface
</pre>


## Credits

### Images

- The banner image was taken from pexel.com: Photo by berffilm: [pexels.com](https://www.pexels.com/photo/hand-reaching-for-cherries-on-tree-19089353/)


### Code & README

- ***My mildew-leaves-detection project is based on the CI's Malaria Detection walkthrough project.***

- I also used the repositories of Claudia Cifaldi and AlbinHall as a reference for the coding, for the README file and for the sturcture of the project:
- [*Claudia Cifaldi*](https://github.com/cla-cif/Cherry-Powdery-Mildew-Detector/)
- [*AlbinHall*](https://github.com/AlbinHall/mildew-detection/)

Thank you guys!!!


### Acknowledgments

- I would like to say a big thank you to my mentor Mo Shami who always pointed me to the right direction, for his availability and for giving me motivation throuhout the whole project. 


- A big thanks again to all the other students in the Slack community who have helped me and inspired me many times.

- Thanks a lot to Kay Welfare for her incredible support that I get every week. 



### Deployed version at [cherry-powdery-mildew-detector.herokuapp.com](https://mildew-leaves-detection-dav-9ff1fd9edf31.herokuapp.com/)