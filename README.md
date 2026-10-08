# Machine Learning-Based Early Prediction of Metabolic Dysfunction-Associated Steatotic Liver Disease

A web-based machine learning prototype for early prediction of MASLD-related risk using non-invasive clinical and lifestyle data.

## Project Overview

Metabolic Dysfunction-Associated Steatotic Liver Disease (MASLD) is a liver condition associated with metabolic risk factors such as obesity, high blood pressure, abnormal glucose levels, and dyslipidemia.

This project develops a machine learning-based web application that accepts non-invasive clinical and lifestyle parameters and predicts whether a person falls into a **lower-risk or higher-risk category** based on a MASLD-related proxy target derived from NHANES data.

The project is developed as an **Advanced Web Technology (AWT) course project**, combining machine learning with a Flask-based web application.

## Dataset

The project uses data from the **National Health and Nutrition Examination Survey (NHANES) 2021–2023**.

Relevant NHANES components used include:

- Demographics
- Body Measurements
- Blood Pressure
- Liver Ultrasound Transient Elastography
- Glucose
- HDL Cholesterol
- Total Cholesterol
- Triglycerides
- Alcohol Use
- Physical Activity

The data files are available in the `masld_data/` directory.

## Features Used

The final machine learning model uses the following features:

- Age
- Sex
- BMI
- Waist Circumference
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Glucose
- HDL Cholesterol
- Total Cholesterol
- Triglycerides
- Sedentary Minutes
- Alcohol Use

## Machine Learning Models

Three classification models were evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 78.71% | 80.00% | 79.48% | 79.74% |
| Decision Tree | 75.81% | 76.80% | 77.54% | 77.17% |
| Random Forest | 77.60% | 77.22% | 81.58% | 79.34% |

**Logistic Regression** was selected as the final model based on its overall performance and simplicity for deployment.

The trained model is stored in:

```text
model/masld_logistic_model.pkl
