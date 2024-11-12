import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_mildew_detector_body():
    st.info(
        f"Here you can upload pictures of cherry leaves to find out whether they are affected by "
        f"powdery mildew and have a look at the report."
        )

    st.write(
        f"At the following Kaggle website:\n\n"
        f"[Cherry Leaves Samples - Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)\n\n"
        f"you can download a set of mixed cherry leaves for an immediate prediction")

    st.write("---")
    
    st.write(
        f"**Please upload a cherry leave picture**"
        )
    images_buffer = st.file_uploader(' ', type='JPG',accept_multiple_files=True)
   
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)

    st.write("---")

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/davidelan/mildew-leaves-detection/blob/main/README.md).")
