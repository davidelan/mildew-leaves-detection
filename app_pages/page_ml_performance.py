import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_body():
    version = 'v1'

    st.header("ML Performance")
    st.info(
        f"This page provides a visually user-friendly illustration of how the dataset was divided "
        f"for the analysis, model training losses and accuracy and"
        f" a generalised performance on test set. ")

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    st.header("Model History")

    st.subheader("Model Training Losses")
    st.image(f"outputs/{version}/model_training_losses.png", caption='Training and Validation Loss')

    st.subheader("Model Training Accuracy")
    st.image(f"outputs/{version}/model_training_acc.png", caption='Training and Validation Accuracy')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.write("---")

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/davidelan/mildew-leaves-detection/blob/main/README.md).")

    
    
    