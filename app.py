import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaf_visualizer import page_leaf_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_body




app = MultiPage(app_name="Cherry Leaf Mildew Detection")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_body)
app.add_page("Leaves Visualiser", page_leaf_visualizer_body)
app.add_page("Mildew Detector", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Machine Learning Performance", page_ml_performance_body)


app.run()  # Run the app