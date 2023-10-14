#!/usr/bin/env python
# coding: utf-8

# In[3]:


import joblib
import streamlit as st
import pandas as pd

loaded_pipe = joblib.load('pipeline.pkl')

import streamlit as st

# Setting page configuration
st.set_page_config(
    page_title='My App',
    page_icon=':chart_with_upwards_trend:',
    layout='wide',
#     theme='light+'
)

# Adding a background image
background_image_style = """
    <style>
        body {
            background-image: url('https://drive.google.com/file/d/1fzRfl1ZZcsZo0O6WPudXnCygg9XKKPTn/view?usp=sharing'); 
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;  
            height: 100vh;  
            width: 100vw;   
        }
    </style>
"""

st.markdown(background_image_style, unsafe_allow_html=True)


st.title('Loan default prediction')
# User input for numerical features
account_type = ['Savings', 'Other', 'Current']
account_type = st.selectbox('Type of bank account', account_type)

bank_options = ['GT Bank', 'First Bank', 'Access Bank', 'Zenith Bank', 'Diamond Bank',
       'UBA', 'FCMB', 'Stanbic IBTC', 'EcoBank', 'Skye Bank', 'Fidelity Bank',
       'Keystone Bank', 'Sterling Bank', 'Union Bank', 'Heritage Bank',
       'Wema Bank', 'Standard Chartered']
bank_name = st.selectbox('Bank name', bank_options)

level_of_education = ['Graduate', 'Secondary', 'Post-Graduate', 'Primary']
education_level = st.selectbox('Level of education', level_of_education)

residence_options = ['Lagos', 'Oyo', 'Ogun', 'Abuja Federal Capital Territory', 'Rivers',
       'Kwara', 'Kaduna', 'Delta', 'Ondo', 'Bayelsa', 'Enugu', 'Edo', 'Imo',
       'Plateau', 'diaspora', 'Cross River', 'Anambra', 'Akwa Ibom', 'Kano',
       'Benue', 'Niger', 'Osun', 'Abia', 'Bauchi', 'Kogi', 'Adamawa',
       'Nasarawa', 'Ekiti', 'Sokoto', 'Ebonyi']
residence = st.selectbox('Place of residence', residence_options)

prev_loan_amount = st.number_input('Previous loan amount', step=1, value=0)
current_loan_amount = st.number_input('Current loan amount', step=1, value=0)

prev_total_due = st.number_input('Previous total due', step=1, value=0)
current_total_due = st.number_input('Current total due', step=1, value=0)

prev_term_days = st.number_input('Previous term days', step=1, value=0)
current_term_days = st.number_input('Current term days', step=1, value=0)

referred_by = st.number_input('Number of people who have referred the client', step=1, value=0)
interest_rate = st.number_input('Interest rate', step=1.0, value=0.0)
prev_time_to_approval = st.number_input('Time taken to approve the previous loan',step=1.0,value=0.0)
current_time_to_approval = st.number_input('Time taken to approve current loan',step=1.0,value=0.0)


age = st.slider('Age', 0, 100, 30)
# User input for categorical features
stability_options = [0,1]
selected_stability = st.selectbox('Employment stability', stability_options)

# Creating a dataframe from the data
input_df = pd.DataFrame({
    'loanamount.prev':[prev_loan_amount],
    'totaldue.prev':[prev_total_due],
    'termdays.prev':[prev_term_days],
    'bank_account_type':[account_type],
    'bank_name_clients':[bank_name],
    'level_of_education_clients':[education_level],
    'customer_residency':[residence],
    'loanamount.perf':[current_loan_amount],
    'totaldue.perf':[current_total_due],
    'termdays.perf':[current_term_days],
    'referredby':[referred_by],
    'interest_rate':[interest_rate],
    'age':[age],
    'time_to_approval.prev':[prev_time_to_approval],
    'time_to_approval.perf':[current_time_to_approval],
    'employment_stability':[selected_stability]        
})
if st.button('Predict'):
    # Use the model to make predictions
    prediction = loaded_pipe.predict(input_df)
    st.write(f'Prediction: {prediction}')

