import numpy as np
import pickle
import joblib
import streamlit as st

# Loading the saved model
#C:\Users\(You need to write your windows username)\Desktop\Final\bank-additional\finalpro.sav
#loaded_model = pickle.load(open(r"finalpro.sav", 'rb'))
loaded_model = joblib.load("finalpro.sav")
# Creating a function for prediction
def bank_marketing_prediction(input_data):
    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    # Map the prediction values to "yes" or "no"
    prediction = "yes" if prediction[0] >=0.48 else "no"

    return prediction


def main():
    # Giving a title
    st.title('Bank Marketing Prediction Web App')

    # Getting input from the user
    age = st.text_input('Age')
    job = st.text_input('Job -> 0 - 10')
    marital = st.text_input('Marital Status -> 0-2')
    education = st.text_input('Education -> 0 - 7')
    default = st.text_input('Default -> 0 or 1')
    housing = st.text_input('Housing -> 0 or 1')
    loan = st.text_input('Loan ->  0 or 1')
    contact = st.text_input('Contact -> 0 or 1')
    month = st.text_input('Month -> 0 - 11 ')
    day_of_week = st.text_input('Day of Week -> 0 - 4')
    duration = st.text_input('Duration')
    campaign = st.text_input('Campaign')
    pdays = st.text_input('Pdays')
    previous = st.text_input('Previous')
    poutcome = st.text_input('Poutcome -> 0 - 2')
    emp_var_rate = st.text_input('Employment Variation Rate')
    cons_price_idx = st.text_input('Consumer Price Index')
    cons_conf_idx = st.text_input('Consumer Confidence Index')
    euribor3m = st.text_input('EURIBOR 3 Month Rate')
    nr_employed = st.text_input('Number of Employees')
    contact_month = 1

    # Code for prediction
    result = ''

    # Getting the input data from the user
    if st.button('Predict'):
        input_data = [age, job, marital, education, default, housing, loan, contact, month, day_of_week,
                      duration, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx,
                      cons_conf_idx, euribor3m, nr_employed, contact_month]
        result = bank_marketing_prediction(input_data)

    st.success(f"Prediction: {result}")


if __name__ == '__main__':
    main()
