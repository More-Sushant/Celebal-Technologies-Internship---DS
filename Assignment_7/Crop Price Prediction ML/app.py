import streamlit as st # type: ignore
import pandas as pd
import pickle
import numpy as np

# Load the model and scaler
with open('./models/Model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('./models/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Function to make predictions
def predict_price(nitrogen, phosphorus, potassium, temperature, humidity, pH_value, rainfall, crop):
    
    input_data = pd.DataFrame([[nitrogen, phosphorus, potassium, temperature, humidity, pH_value, rainfall, crop]])
    
    input_scaled = scaler.transform(input_data)
    predicted_price = model.predict(input_scaled)
    
    return predicted_price[0] 

st.title('Crop Price Prediction App')
st.write('Enter the following parameters to predict the crop price:')


nitrogen = st.number_input('Nitrogen', min_value=0.0)
phosphorus = st.number_input('Phosphorus', min_value=0.0)
potassium = st.number_input('Potassium', min_value=0.0)
temperature = st.number_input('Temperature (°C)')
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0)
pH_value = st.number_input('pH Value', format="%.2f")
rainfall = st.number_input('Rainfall (mm)', min_value=0.0,)


crop = st.selectbox('Crop', options=[ '1','2','3','4','5','6','7','8','9','10','11','12','13','14', '15', '16','17', '18','19','20']) 



if st.button('Predict Price'):
    price = predict_price(nitrogen, phosphorus, potassium, temperature, humidity, pH_value, rainfall, crop)
    st.write(f'The predicted price for the crop is: ${price:.2f}')
