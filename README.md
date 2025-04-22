# Alzheimer's Disease Progression Prediction with LSTM-Attention

## Project Overview
This project focuses on developing a deep learning model to predict the progression of Alzheimer's disease using real-world, longitudinal patient data. By leveraging a combination of clinical, demographic, and genetic data, the model captures the temporal evolution of the disease and the nuanced effects of APOE genotypes. We use an LSTM network with attention mechanisms to process irregular visit intervals and provide interpretable insights for clinical use.

## Key Features
- **Dynamic Temporal Padding:** Handles variable-length visit sequences and normalizes time intervals to address irregular data.
- **Genetic Embedding Matrix:** Encodes APOE alleles as learnable embeddings for more accurate genotype modeling.
- **Hybrid Imputation:** Robustly deals with missing data, including imputed genotypes.
- **LSTM-Attention Model:** Focuses on the most relevant patient visits for disease progression prediction.
- **Interactive Attention Tools:** Provides clinicians with transparent visualizations of model decision-making.

## Dataset
This project uses a subset of the Alzheimer’s Disease Neuroimaging Initiative (ADNI) dataset, including MRI scans and clinical data such as age, gender, education, MMSE score, and APOE genotype.

## Objective
To build a deep learning model capable of:
- Predicting Alzheimer’s progression from as few as one clinical visit.
- Embedding genetic data (APOE alleles) for accurate disease risk modeling.
- Ensuring interpretability and clinical applicability through attention mechanisms and interactive tools.

## Methodology
- Data preprocessing with SMOTE for class imbalance, normalization, and temporal feature engineering.
- LSTM-Attention network to process patient visit sequences with dynamic padding.
- Genetic data encoding through embedding layers to capture complex APOE genotype effects.

## Live Web Application
You can explore the live web application for Alzheimer’s progression prediction built using Streamlit and deployed on Streamlit Community Cloud. Access it here:  
[Alzheimer's Progression Prediction Streamlit App](https://pratham2203-alzheimers-prediction-streamlit-app-hxofzr.streamlit.app)

## Contributing
Feel free to open issues or submit pull requests for improvements. Contributions are welcome!
