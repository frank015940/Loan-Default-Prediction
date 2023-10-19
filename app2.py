import streamlit as st
import pandas as pd
import numpy as np
import joblib 
import pickle


#loaded_pipe = joblib.load('ensemble_pipeline.pkl',allow_pickle=True)

with open('decision_tree_model.pkl', 'rb') as f:
    loaded_pipe = pickle.load(f)


#st.set_page_config(
    #page_title='Loan Default Prediction App',
    ##page_icon=':moneybag:',  # You can choose an appropriate icon
    #layout='centered',  # You can use 'centered' for a centered layout
    #initial_sidebar_state='expanded'  # Keep the sidebar expanded by default
#)
# Setting page configuration

st.set_page_config(
    page_title="Loan Default Prediction App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)


# Add some CSS styles for a cleaner look
#st.markdown(
 #   """
    #<style>
    #body {
    #    background-color: #000000;  /* Set your preferred background color */
    #    font-family: Arial, sans-serif;  /* Choose a professional font */
    #}
    #.sidebar .sidebar-content {
    #    background-color: #333333;  /* Change the sidebar color */
    #    color: white;  /* Text color in the sidebar */
    #}
    #.css-17v4k9n {
    #    color: #333333;  /* Change text color in the main content area */
    #}
    #</style>
    #""",
    #unsafe_allow_html=True
#)

st.markdown(
    """
    <style>
    body {
        background-color: #000;  /* Black background color */
        color: white;  /* White text color */
        font-family: Arial, sans-serif;  /* Choose a professional font */
    }
    .sidebar .sidebar-content {
        background-color: #333;  /* Change the sidebar color */
        color: white;  /* Text color in the sidebar */
    }
    .css-17v4k9n {
        color: white;  /* Change text color in the main content area */
    }
    .stButton > button {
        background-color: green;  /* Green button background color */
        color: white;  /* White text color for buttons */
    }
    </style>
    """,
    unsafe_allow_html=True
)


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

# Define a function to assign credit scores
def assign_credit_score(percentages):
    credit_scores = {}
    for category, (bad_percentage, good_percentage) in percentages.items():
        # Assign higher scores to categories with higher 'Good' (non-default) percentages
        credit_scores[category] = good_percentage

    # Normalize credit scores to a scale of 1 to 100
    max_score = max(credit_scores.values())
    min_score = min(credit_scores.values())
    normalized_scores = {category: 1 + 99 * ((score - min_score) / (max_score - min_score)) for category, score in credit_scores.items()}

    return normalized_scores


if st.button('Predict'):
    # Use the model to make predictions
    prediction = loaded_pipe.predict(input_df)
    st.write(f'Prediction: {prediction}')

    # Calculate and display the credit score
    credit_scores = assign_credit_score({'Credit Category': (0.2, 0.8)})  # Modify this as per your logic
    st.write(f'Credit Score: {credit_scores["Credit Category"]}')