import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("shortlisting_model.pkl")

st.title("🤖 AI Resume Screening System")

st.write("Enter candidate details:")

# Inputs
exp = st.slider("Years of Experience", 0, 20, 2)
skills = st.slider("Skills Match Score", 0, 100, 50)
edu = st.selectbox("Education Level", ["High School", "Bachelors", "Masters", "PhD"])
projects = st.slider("Project Count", 0, 20, 3)
length = st.slider("Resume Length", 100, 3000, 1000)
github = st.slider("GitHub Activity", 0, 100, 20)

# Encoding
edu_map = {'High School': 0, 'Bachelors': 1, 'Masters': 2, 'PhD': 3}

if st.button("Predict"):
    input_data = np.array([[exp, skills, edu_map[edu], projects, length, github]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Shortlisted")
    else:
        st.error("❌ Not Shortlisted")
