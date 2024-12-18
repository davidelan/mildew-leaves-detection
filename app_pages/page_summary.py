import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Project Summary")

    st.info(
f"**General Information**\n\n"
f"Powdery mildew, caused by the fungus Podosphaera clandestina, is a common and damaging " 
f"disease affecting cherry trees. This parasitic fungus manifests as a white, powdery layer on the " 
f"leaves, primarily targeting new growth and potentially extending to the fruit itself. As the " 
f"infection progresses, it can lead to significant crop loss, hindering both the growth of the plants " 
f"and the quality of the harvest.\n\n"
f"Detecting powdery mildew in cherry orchards can be a daunting task, especially given the large " 
f"number of trees involved. Traditional manual inspection is often insufficient and impractical. To " 
f"address this challenge, researchers are turning to advanced technology, specifically machine " 
f"learning, to revolutionize how farmers monitor their orchards. "
f"The proposed solution involves developing a sophisticated model capable of analyzing cherry leaf " 
f"images to differentiate between healthy and infected specimens. Key visual indicators for " 
f"identifying powdery mildew include light-green circular lesions on the leaves, which later develop " 
f"into a cotton-like growth. This automated approach promises to enhance early detection, allowing " 
f"for timely intervention and more effective disease management. "
f"By leveraging deep learning techniques, this initiative aims to provide cherry growers with an " 
f"efficient, scalable tool to combat powdery mildew. This technological advancement could " 
f"significantly improve both crop yield and quality, paving the way for healthier orchards and a " 
f"more sustainable agricultural future. \n\n"   
    )

    st.warning(
        f"**Project Dataset**\n\n"
        f"This project uses a dataset of cherry leaf images provided by Farmy & Foods. " 
        f"The images were carefully gathered and labeled to guarantee the accuracy and reliability of the model "
        f"during training."
        )

    st.success(
        f"**Business Requirements**\n\n"
    
        f"1 - Visually differentiate a healthy cherry leaf from an infected one.\n\n"
        f"2 - An accurate prediction whether a given cherry leaf is infected by powdery mildew or not. \n\n"
        f"3 - Download a prediction report of an examination of cherry leaves."
        )

    st.write("---")

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/davidelan/mildew-leaves-detection/blob/main/README.md).")
