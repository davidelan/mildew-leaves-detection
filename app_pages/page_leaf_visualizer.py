import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_leaf_visualizer_body():
    st.write("### Leaves Visualizer")
    st.info(
        f"The purpose of this study is to help distinguish between "
        f"a healthy cherry leaf and one affected by mildew.\n\n"

        f"This page provides a visual representation of the cherry leaf dataset."
        
        f"Below you have the opportunity to explore differen kind of visualizations and "
        f"get a better understanding between healthy and unhealthy cherry leaves.")

    st.write("---")

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/davidelan/mildew-leaves-detection/blob/main/README.md).")

    st.write("---")

    version = 'v1'

    if st.checkbox("Samples Cherry Leaf Image"):
        col1, col2 = st.beta_columns(2)
        with col1:
         st.image(f"outputs/{version}/sample_healthy_leaf.png", caption='Sample Cherry healthy Leaf Image')
        with col2:
         st.image(f"outputs/{version}/sample_mildew_leaf.png", caption='Sample Cherry mildew Leaf Image')


    if st.checkbox("Difference between average and variability image"):
      
      avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

      st.warning(
        f"As you can see below, the average and variability images did not reveale clear patterns "
        f"which could allow us to intuitively distinguish from the two categories.")

      st.image(avg_powdery_mildew, caption='Mildew leaf - Average and Variability')
      st.image(avg_uninfected, caption='Healthy leaf - Average and Variability')
      st.write("---")

    if st.checkbox("Differences between average infected and average healthy leaves"):
          diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")


          st.warning(
            f"The first pair of images represents the mean value. "
            f"Concerning variability differences, the darker areas indicate regions where the two images "
            f"are similar, while the lighter areas show areas with differing variability.")
          st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("Choose a label from the dropdown menu to create a montage of images from the two categories")
      my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        image_montage(dir_path= my_data_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10,25))
      st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    # how many images in that folder
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)
    # plt.show()


  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")