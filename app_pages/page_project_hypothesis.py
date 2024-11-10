import streamlit as st


def page_project_hypothesis_body():

    st.write("""
    The core hypothesis of this project is that a machine learning model, particularly a Convolutional 
    Neural Network (CNN), can be trained to precisely identify cherry leaf images as either healthy 
    or infected with powdery mildew. The model will be capable of detecting subtle visual signs of 
    mildew infection that are usually very difficult or impossible for the humans to determine, 
    especially during the initial stages of the infection..
    """)

    st.info("""
    ## Hypothesis
    1. **Features of Infected Leaves**: The hypothesis is that infected leaves show dinstinct 
    characteristics, which give space for a consistent differentiation. Specifically, 
    coloration patterns and textures in the images are a very suitable candidate for 
    Convolutional Neural Network (CNN) model investigation.

    2. **Efficiency**: The machine learning system is designed to greatly speed up the 
    process of cherry leaf analysis. By automating the identification of powdery mildew, the tool 
    can save a significant amount of time, labor, and financial resources compared to traditional 
    manual inspections. With an estimated very high accuracy rate, it is expected to cut down 
    inspection time and resource use by up to 90%.

    3. **Human Error**: Human inspections of cherry leaves are often susceptible to mistakes, such as 
    missing early indicators of disease. This model aims to reduce such errors by uniformly applying 
    detection criteria, ensuring more consistent and precise outcomes. This feature is especially 
    beneficial for large-scale operations with a high volume of leaves to examine.

    4. **Prevention and Early Detection**: Identifying powdery mildew early is essential to stopping 
    its spread across a large orchard. The model is thought to outperform human inspectors in spotting 
    the initial signs of infection, enabling faster intervention. Early detection can lead to more 
    effective treatment, better management practices, and ultimately safeguard both crop yield and 
    quality.

    5. **Financial Impact**: Integrating this machine learning solution into agricultural practices 
    offers businesses the chance to enhance their crop management strategies. The ability to quickly 
    and accurately detect infected leaves allows for quicker action, lowering the risk of widespread 
    disease and offering substantial potential for cost savings.
    """)

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/davidelan/mildew-leaves-detection/blob/main/README.md).")