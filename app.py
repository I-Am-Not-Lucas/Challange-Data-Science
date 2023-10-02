import streamlit as st
import pandas as pd
from category_encoders import CatBoostEncoder
from PIL import Image
import pickle

#import seaborn as sns
#import matplotlib.pyplot as plt


### Configurações streamlit

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

## Caminhos
CATBOOST_ENCODER_PATH = "Catboost_Encoder.pkl"

def trata_dados(dados_brutos):
    
    colunas_originais = [ 'customer.gender', 
           'customer.SeniorCitizen',
       'customer.Partner', 
       'customer.Dependents', 
       'customer.tenure',
       'phone.PhoneService', 
       'phone.MultipleLines', 
       'internet.OnlineSecurity', 
       'internet.OnlineBackup',
       'internet.DeviceProtection', 
       'internet.TechSupport',
       'internet.StreamingTV', 
       'internet.StreamingMovies', 
       'account.PaperlessBilling',
       'account.Charges.Monthly']

    catboost_importado = pickle.load(open(CATBOOST_ENCODER_PATH, 'rb'))

    dataframe = pd.DataFrame([dados_brutos.values()], columns=dados_brutos.keys())
  
    dicionario = {'No internet service':0,
                  'No phone service': 0,
                  'No': 0,
                  'Yes': 1,
                  'Male': 0,
                  'Female': 1}

    dicionario2 = {'payment_method': 'account.PaymentMethod',
                'contract': "account.Contract",
                'internet_service': 'internet.InternetService'}
    

    



    colunas_multiclasses = ['internet.InternetService', 
                        'account.Contract',
                        'account.PaymentMethod']



    ##Segundo tratamento
    dataframe[colunas_originais] = dataframe[colunas_originais].replace(dicionario)

    dataframe.rename(columns=dicionario2, inplace=True)

    dataframe[colunas_multiclasses] = catboost_importado.transform(dataframe[colunas_multiclasses]) 




    return dataframe

## Imagens
image = Image.open('identidade visual/PNG/Logo3.png')
st.image(image)


aba1, aba2= st.tabs(["IA", "DASHBOARD"])


with aba2:
    st.markdown("<h2 style='text-align: center;'>Em construção</h1>", unsafe_allow_html=True)


with aba1: 
    #Imagem novexus
    
    
    st.markdown("<h3 style='text-align: center;'>Modelo de previsão de churn</h3>", unsafe_allow_html=True)


    data_stranger = {}
    col1, col2, col3 = st.columns(3)


    with col1:
        data_stranger['customer.gender'] = st.selectbox('Gender:', GENDER_OPTIONS)
        data_stranger['customer.SeniorCitizen'] = st.selectbox('Senior Citizen:', SENIOR_CITIZEN_OPTIONS)
        data_stranger['customer.Partner'] = st.selectbox('Customer Partner:', CUSTOMER_PARTNER_OPTIONS)
        data_stranger['customer.Dependents'] = st.selectbox('Customer Dependents:', CUSTOMER_DEPENDENTS_OPTIONS)
        data_stranger['customer.tenure'] = st.number_input('Customer Tenure:', min_value=0, max_value=100, value=18)
        data_stranger['phone.PhoneService'] = st.selectbox('Phone Service:', PHONE_SERVICE_OPTIONS)

    with col3:
        data_stranger['phone.MultipleLines'] = st.selectbox('Multiple Lines:', MULTIPLE_LINES_OPTIONS)
        data_stranger['internet.InternetService'] = st.selectbox('Internet Service:', INTERNET_SERVICE_OPTIONS)
        data_stranger['internet.OnlineSecurity'] = st.selectbox('Online Security:', ONLINE_SECURITY_OPTIONS)
        data_stranger['internet.OnlineBackup'] = st.selectbox('Online Backup:', ONLINE_BACKUP_OPTIONS)
        data_stranger['internet.DeviceProtection'] = st.selectbox('Device Protection:', DEVICE_PROTECTION_OPTIONS)
        data_stranger['internet.TechSupport'] = st.selectbox('Tech Support:', TECH_SUPPORT_OPTIONS)

    with col2:
        data_stranger['internet.StreamingTV'] = st.selectbox('Streaming TV:', STREAMING_TV_OPTIONS)
        data_stranger['internet.StreamingMovies'] = st.selectbox('Streaming Movies:', STREAMING_MOVIES_OPTIONS)
        data_stranger['account.Contract'] = st.selectbox('Contract:', CONTRACT_OPTIONS)
        data_stranger['account.PaperlessBilling'] = st.selectbox('Paperless Billing:', PAPERLESS_BILLING_OPTIONS)
        data_stranger['account.PaymentMethod'] = st.selectbox('Payment Method:', PAYMENT_METHOD_OPTIONS)
        data_stranger['account.Charges.Monthly'] = st.number_input('Monthly Charges:', min_value=0, max_value=100, value=18)
    

    modelo_importado = pickle.load(open("best_model2.pkl", "rb"))

    dados_tratados = trata_dados(data_stranger)
    prediction = modelo_importado.predict(dados_tratados)
    
    # extra: probabilidade de churn
    probability = modelo_importado.predict_proba(dados_tratados)


    #st.dataframe(dados_tratados)
    if st.button('Fazer previsão'):
        
        
        st.markdown("<h3 style='text-align: center;'>Resultado da previsão</h3>", unsafe_allow_html=True)  
        
        if prediction[0] == 0:
            st.error('Churn: Não', icon="❌")
        else:
            st.success('Churn: Sim', icon="✅")
                
        st.progress(probability[0][1], text=f':black[Probabilidade de churn: {100*probability[0][1]:.2f}%]')

