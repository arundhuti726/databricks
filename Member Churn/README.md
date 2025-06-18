# 🩺 Healthcare Insurance Member Churn – Feature Engineering & Prediction

This project focuses on building a machine learning–ready dataset and predicting churn behavior among healthcare insurance members. Using PySpark in Databricks, the solution implements a complete data pipeline from raw data ingestion to cleaning, feature engineering, and logistic regression modeling.

---

## 🔍 Objective

To identify high-risk churn members by engineering features from raw healthcare data and training a predictive model using scalable, reproducible PySpark workflows on the Databricks Lakehouse platform.

---

## 📁 Data Schema

The raw dataset contains the following fields:

| Column Name | Data Type | Description |
|-------------------------|-----------|---------------------------------------------|
| `member_id` | string | Unique ID for each member |
| `age` | integer | Age of the member |
| `gender` | string | Gender (Male/Female/Null) |
| `tenure_months` | integer | Number of months enrolled |
| `chronic_condition` | integer | 1/2/3 category to indicate chronic severity |
| `claim_count` | integer | Total number of claims filed |
| `total_claim_amount` | double | Total amount claimed |
| `premium_increase_pct` | double | Premium increase percentage |
| `late_payment` | integer | Count of late payments |
| `customer_service_call` | integer | Number of support calls made |
| `churned` | string | Target variable (`True`/`False`) |

---

## ⚙️ Pipeline Overview

### 1. 🔹 **Raw Data Ingestion & Cleaning (Bronze ➡ Silver)**

- Read raw data from file location
- Analyzed schema using `printSchema()` and `display()`
- Converted literal `'NULL'` strings to actual null values
- Imputed missing numeric fields with mean values
- Created imputation flag columns (e.g., `age_imputed`)
- Saved cleaned data to Delta Lake in Silver layer with schema merge enabled

### 2. 🔸 **Feature Engineering**

- **Age Bucketing**: Grouped members by age ranges (`<30`, `30–45`, `45–60`, etc.)
- **Gender Encoding**:
- Male → 1, Female → 0, Null kept as is
- Also used `StringIndexer` with `handleInvalid="skip"` to create `gender_index`
- **Standardization**:
- Applied `VectorAssembler` and `StandardScaler` on `total_claim_amount`
- Extracted and stored `total_claim_amount_scaled`
- **High Risk Flag**:
- Custom logic applied based on claim, age, and tenure to assign `high_risk_flag`
- Resulting feature set written again to the Silver layer

### 3. 🧠 **Churn Prediction Using Logistic Regression**

- Train-test split (80/20) with fixed random seed
- Applied:
- `StringIndexer` for `churned` → `label_index`
- `VectorAssembler` to create `features` column
- Trained Logistic Regression model using Spark MLlib
- Created ML Pipeline:
- Indexers → Assembler → Logistic Regression
- Model fitted, saved, reloaded, and applied to predict churn
- Predictions included: `prediction`, `probability`, `rawPrediction`

---

## 📊 Insights & Applications

The final predictions helped identify:
- **Members at high churn risk**
- **Key predictors of churn**, like:
- Lower tenure
- High premium increase
- Chronic conditions
- High claim or customer service call volume

This approach supports:
- Retention strategies
- Personalized outreach
- Preventative care targeting for high-risk members

---

## 🧱 Tech Stack

- **Databricks (Lakehouse)**
- **PySpark**
- **Delta Lake**
- **Spark MLlib**
- **Notebook Modularization (ETL / Feature Engineering / Modeling)**

---

## 🗃️ Folder Structure
member-churn-ml/
│
├── notebooks/
│   ├── 1_data_ingestion_cleaning.ipynb
│   ├── 2_feature_engineering.ipynb
│   └── 3_churn_prediction_model.ipynb
│
├── data/                       # (optional sample data)
│
├── README.md
└── requirements.txt           # (if needed for local Spark setup)
