<img width="1257" height="805" alt="image" src="https://github.com/user-attachments/assets/f7ddb21e-f4a4-49e1-8f84-876796803783" />

#  AI Resume Screening System

An intelligent Machine Learning-based system that automates the process of candidate shortlisting using structured resume features. This project demonstrates how ML can assist HR teams in making faster and data-driven hiring decisions.

---

##  Overview

Manual resume screening is time-consuming, inconsistent, and prone to human bias.  
This project solves that problem by using a trained machine learning model to predict whether a candidate should be shortlisted based on key attributes.

The system is deployed as an interactive web application using Streamlit.

---

##  Features

-  Automated candidate shortlisting  
-  Machine Learning model (Random Forest Classifier)  
-  Fast predictions based on input features  
-  Interactive web UI using Streamlit  
-  Model evaluation with accuracy, precision, recall, and F1-score  
-  Cross-validation for performance stability  

---

##  Machine Learning Pipeline

Data Collection → Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment


---

##  Dataset

The dataset consists of structured candidate information:

| Feature | Description |
|--------|------------|
| years_experience | Candidate's work experience (in years) |
| skills_match_score | Skill relevance score (0–100) |
| education_level | Education qualification |
| project_count | Number of projects completed |
| resume_length | Length of resume |
| github_activity | GitHub contribution/activity score |
| shortlisted | Target variable (Yes/No) |

---

##  Tech Stack

- Python   
- Scikit-learn  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Streamlit (for UI)  

---

##  Model Details

- Algorithm: **Random Forest Classifier**
- Training Accuracy: ~92%
- Testing Accuracy: ~90%
- Cross-Validation Accuracy: ~90.5%

The model demonstrates strong generalization with minimal overfitting.

---

##  Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  

---

##  Web Application

The project includes a Streamlit-based UI where users can input candidate details and get instant predictions.

>  Note: Inputs in the UI simulate features that would typically be extracted automatically from resumes using NLP techniques in a real-world system.

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/resume-screening-ml.git
cd resume-screening-ml
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the application
``` bash
streamlit run app.py
```
### Deployment

The application is deployed using Streamlit Cloud and can be accessed via a public URL.

### Future Enhancements
Resume PDF upload & parsing (NLP-based)
Skill extraction using NLP techniques
Integration with real HR systems
Advanced models like XGBoost / Deep Learning

### References
Scikit-learn Documentation
Streamlit Documentation
Kaggle Datasets

### Author

Developed as part of a Machine Learning academic project.

### Acknowledgements

Special thanks to open-source tools and datasets that made this project possible.
