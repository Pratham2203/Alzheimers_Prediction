import streamlit as st
from config import BANNER

def home_page():
    st.image(BANNER)
    st.write("""
        ## Introduction to Alzheimer's Disease
        Alzheimer's disease (AD) is a progressive neurodegenerative disease. Though best known for its role in declining memory function, symptoms also include: difficulty thinking and reasoning, making judgements and decisions, and planning and performing familiar tasks. It may also cause alterations in personality and behavior. The cause of AD is not well understood. There is thought to be a significant hereditary component. For example, a variation of the APOE gene, APOE e4, increases risk of Alzheimer's disease.

        ## Why Early Detection Matters
        Early detection of Alzheimer's disease is paramount because it offers the best chance for effective treatment and improved quality of life. Identifying the condition at its onset allows for timely interventions, which can slow its progression and enable individuals and their families to plan for the future. Early detection also facilitates access to support services and clinical trials, fostering hope for more effective therapies in the fight against this devastating disease.

        ## Purpose of the project
        The purpose of this project is to develop a deep learning model for predicting the progression of Alzheimer's disease using real-world, longitudinal patient data. Alzheimer's disease is a complex and slowly progressing neurodegenerative disorder, and early, accurate detection is essential for effective intervention and patient care. This project aims to leverage an LSTM model with attention mechanisms to analyze patient visit sequences, incorporating clinical, demographic, and genetic data (such as APOE genotype). The goal is to create a model that not only predicts disease progression but also provides interpretable insights, enabling clinicians to make informed decisions based on irregular and incomplete patient data.
        
        <br>
                
        """, unsafe_allow_html=True)

    st.caption('Finished reading? Navigate to the `Prediction Page` to make some predictions')