import streamlit as st
import pandas as pd

#import pickle
#import seaborn as sns
#import matplotlib.pyplot as plt
from PIL import Image

## Configurações streamlit

## Tabela de opções
GENDER_OPTIONS = ['Female', 'Male']
SENIOR_CITIZEN_OPTIONS = ['No', 'Yes']
CUSTOMER_PARTNER_OPTIONS = ['No', 'Yes']
CUSTOMER_DEPENDENTS_OPTIONS = ['No', 'Yes']
PHONE_SERVICE_OPTIONS = ['No', 'Yes']
MULTIPLE_LINES_OPTIONS = ['No', 'Yes', 'No phone service']
INTERNET_SERVICE_OPTIONS = ['DSL', 'Fiber optic', 'No']
ONLINE_SECURITY_OPTIONS = ['No', 'Yes', 'No internet service']
ONLINE_BACKUP_OPTIONS = ['No', 'Yes', 'No internet service']
DEVICE_PROTECTION_OPTIONS = ['No', 'Yes', 'No internet service']
TECH_SUPPORT_OPTIONS = ['No', 'Yes', 'No internet service']
STREAMING_TV_OPTIONS = ['No', 'Yes', 'No internet service']
STREAMING_MOVIES_OPTIONS = ['No', 'Yes', 'No internet service']
CONTRACT_OPTIONS = ['One year', 'Month-to-month', 'Two year']
PAPERLESS_BILLING_OPTIONS = ['Yes', 'No']
PAYMENT_METHOD_OPTIONS = ['Mailed check', 'Electronic check', 'Credit card (automatic)', 'Bank transfer (automatic)']

def trata_dados(dataframe):
    dataframe = dataframe.replace()



aba1, aba2= st.tabs(["IA", "DASHBOARD"])


with aba2:
    st.markdown("<h2 style='text-align: center;'>Em construção</h1>", unsafe_allow_html=True)


with aba1: 
    #Imagem novexus
    image = Image.open("identidade visual\PNG\Logo (2).png")
    st.image(image, use_column_width=True)
    st.markdown("<h3 style='text-align: center;'>Modelo de previsão de churn</h3>", unsafe_allow_html=True)


    data_stranger = {}
    col1, col2, col3 = st.columns(3)



    with col1:
        data_stranger['customer_gender'] = st.selectbox('Gender:', GENDER_OPTIONS)
        data_stranger['customer_senior_citizen'] = st.selectbox('Senior Citizen:', SENIOR_CITIZEN_OPTIONS)
        data_stranger['customer_partner'] = st.selectbox('Customer Partner:', CUSTOMER_PARTNER_OPTIONS)
        data_stranger['customer_dependents'] = st.selectbox('Customer Dependents:', CUSTOMER_DEPENDENTS_OPTIONS)
        data_stranger['customer_tenure'] = st.number_input('Customer Tenure:', min_value=0, max_value=100, value=18)
        data_stranger['phone_service'] = st.selectbox('Phone Service:', PHONE_SERVICE_OPTIONS)

    with col3:
        data_stranger['multiple_lines'] = st.selectbox('Multiple Lines:', MULTIPLE_LINES_OPTIONS)
        data_stranger['internet_service'] = st.selectbox('Internet Service:', INTERNET_SERVICE_OPTIONS)
        data_stranger['online_security'] = st.selectbox('Online Security:', ONLINE_SECURITY_OPTIONS)
        data_stranger['online_backup'] = st.selectbox('Online Backup:', ONLINE_BACKUP_OPTIONS)
        data_stranger['device_protection'] = st.selectbox('Device Protection:', DEVICE_PROTECTION_OPTIONS)
        data_stranger['tech_support'] = st.selectbox('Tech Support:', TECH_SUPPORT_OPTIONS)

    with col2:
        data_stranger['streaming_tv'] = st.selectbox('Streaming TV:', STREAMING_TV_OPTIONS)
        data_stranger['streaming_movies'] = st.selectbox('Streaming Movies:', STREAMING_MOVIES_OPTIONS)
        data_stranger['contract'] = st.selectbox('Contract:', CONTRACT_OPTIONS)
        data_stranger['paperless_billing'] = st.selectbox('Paperless Billing:', PAPERLESS_BILLING_OPTIONS)
        data_stranger['payment_method'] = st.selectbox('Payment Method:', PAYMENT_METHOD_OPTIONS)
        data_stranger['monthly_charges'] = st.number_input('Monthly Charges:', min_value=0, max_value=100, value=18)
    
