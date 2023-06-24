import streamlit as st
from prediction import predict_yield
import numpy as np

st.set_page_config(page_title="Wild Blueberry Yield Prediction App",
                   page_icon="🍇", layout="wide")

col1, col2 = st.columns([3, 5])
# ['clonesize', 'bumbles', 'adrena', 'osmia', 'MaxOfUpperTRange', 'RainingDays', 'fruitset', 'fruitmass','seeds']

with col1:
    with st.form("prediction_form"):
        st.header("Enter the Deciding Factors:")

        clonesize = st.text_input("Blueberry clonesize value")
        bumbles = st.text_input("Bumblebee density value")
        adrena = st.text_input("Adrena bee density value")
        osmia = st.text_input("Osmia bee density value")
        AverageOfLowerTRange = st.text_input("max-upper temperature Range")
        AverageRainingDays = st.text_input("Raining days value")
        submit_val = st.form_submit_button("Predict Yield")

if submit_val:
    #print(clonesize)
    attribute = np.array([float(clonesize), float(bumbles), float(adrena), float(osmia),
                          float(AverageOfLowerTRange), float(AverageRainingDays)]).reshape(1, -1)

    if attribute.shape == (1, 6):
        print("Attributes are Valid")

        value = predict_yield(attributes=attribute)

        with col2:
            st.header("Here are the results:")
            st.success(f"The yield value is {value}")