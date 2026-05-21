
import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

st.title("Telco Customer Churn Prediction (Pretrained AutoML Model)")

# Load test data
test = pd.read_csv("test.csv")

# Load pretrained model
model = load_model("best_automl_model")  # assumes best_automl_model.pkl exists in the same folder

# Prediction and download
if st.button("Run Predictions"):
    predictions = predict_model(model, data=test)
    submission = pd.DataFrame({
        "Churn_Predicted": predictions["prediction_label"]
    })
    submission.to_csv("submission.csv", index=False)
    st.success("Predictions completed successfully.")
    st.download_button(
        label="Download Prediction File",
        data=open("submission.csv", "rb"),
        file_name="submission.csv",
        mime="text/csv"
    )

