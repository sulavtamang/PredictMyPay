import joblib
import os
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app/utils/

MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "models", "predictor_model.pkl"))
SCALER_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "models", "input_scaler.pkl"))

print(BASE_DIR)

edu_map = {"High School": 0, "Bachelor's Degree": 1, "Master's Degree": 2, "PhD": 3}

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_resource
def load_scaler():
    return joblib.load(SCALER_PATH)

def predict_salary(age, experience, education_level, job_role):
    model = load_model()
    scaler = load_scaler()

    job_role = job_role.lower()
    if 'junior' in job_role:
        role_seniority = 0
    elif 'senior' in job_role:
        role_seniority = 2
    elif 'manager' in job_role:
        role_seniority = 3
    elif 'director' in job_role:
        role_seniority = 4
    else:
        role_seniority = 1

    edu_code = edu_map.get(education_level, 0)

    input_data = pd.DataFrame(
    [[age, experience, edu_code, role_seniority]],
    columns=["experience_years", "age", "education_encoded", "seniority_encoded"])

    input_scaled = scaler.transform(input_data)
    predicted_salary = model.predict(input_scaled)[0]
    
    return predicted_salary
