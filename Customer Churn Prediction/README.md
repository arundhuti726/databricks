**# ML Readiness Pipeline: Telco Customer Churn**

📌 **Project Overview**  
This project focuses on preparing Telco Customer Churn data for Machine Learning using **PySpark** and **Delta Lake** on **Azure Databricks**. The end goal is to clean, transform, and engineer features for model readiness, including embedding categorical variables using **Word2Vec**.

📊 **Dataset Source**  
The dataset used is `TelcoCustomerChurn.csv`, obtained from **Kaggle**. It includes customer-level data from a telecom provider to predict churn behavior.

📁 **Column Descriptions**  
`customerID`, `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`, `Churn`.

🛠️ **Workflow Summary**
- Ingest raw data and save in **Bronze** layer  
- Clean and handle missing/null values (strings, integers, doubles)  
- Typecast appropriate fields (e.g., `SeniorCitizen` and `Churn` to Boolean)  
- Write cleaned data into Delta format in **Silver** layer  
- Split dataset into 80/20 Train/Test sets with `seed=42`  
- Feature engineering using **Word2Vec** on categorical columns  
- Apply embeddings and assemble feature vectors  
- Register the transformed data for ML consumption  

🚀 **Azure Databricks Job Deployment**  
Each step is modularized into separate notebooks and deployed as a multi-task **Azure Databricks Job**:
1. Raw Data Ingestion → Bronze Layer  
2. Data Cleaning & Type Casting → Silver Layer  
3. Feature Engineering with Embeddings → Final Train/Test Sets  

🧰 **Tech Stack**
- **Platform:** Azure Databricks  
- **Language:** PySpark  
- **Storage:** Delta Lake  
- **ML Tool:** Word2Vec embeddings  

✅ **Output**  
The final output includes **ML-ready train and test datasets** with numeric and embedded categorical features, stored in **Delta format** and ready for model training pipelines.
