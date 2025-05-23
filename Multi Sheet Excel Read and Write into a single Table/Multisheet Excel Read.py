# Databricks notebook source
#dbutils.fs.mv("dbfs:/user/arundhuti/delta/Read.xlsx","dbfs:/user/hive/")

# COMMAND ----------

import os  # Import the os module for interacting with the operating system
import json  # Import the json module for working with JSON data
from pyspark.sql.types import StructType, StructField, StringType, MapType  # Import necessary Spark SQL types
from pyspark.sql.functions import col, explode, lit  # Import necessary Spark SQL functions
import pandas as pd  # Import pandas for data manipulation

# Define Schema 
mapSchema = StructType([
    StructField("Key", StringType(), True),  # Define a StringType field for the key
    StructField("Value", MapType(StringType(), StringType()), True),  # Define a MapType field for the value
])

maptypeData = []  # Initialize an empty list to store map type data
source = '/dbfs/user/arundhuti/delta/'  # Define the source directory
file_type = 'xlsx'  # Define the file type to look for
list_files = os.listdir(source)  # List all files in the source directory
global acc  # Declare a global variable 'acc'

for file in list_files:  # Iterate over each file in the directory
    if file.endswith(file_type):  # Check if the file is of the specified type
        file_path = os.path.join(source, file)  # Get the full file path
        fileName = file  # Get the file name
        baseName, extension = os.path.splitext(fileName)  # Split the file name and extension
        xls = pd.ExcelFile(file_path)  # Load the Excel file
        sht_name = xls.sheet_names  # Get the sheet names in the Excel file
        acc = 0  # Initialize the sheet counter
        for s in sht_name:  # Iterate over each sheet name
            data = pd.read_excel(xls, s)  # Read the sheet data into a Pandas DataFrame
            df = spark.createDataFrame(data)  # Convert the Pandas DataFrame to a Spark DataFrame
            val = {}  # Initialize an empty dictionary to store row data
            if s.__contains__('Sheet'):  # Check if the sheet name contains 'Sheet'
                s = 'other' + '_' + str(acc)  # Rename the sheet
                acc += 1  # Increment the sheet counter
            else:
                s = s  # Keep the original sheet name
            
            ky = baseName + '_' + s  # Create a key using the base name and sheet name
            col = df.count()  # Get the number of rows in the DataFrame
            row = len(df.columns)  # Get the number of columns in the DataFrame
            df_data = df.collect()  # Collect the DataFrame data as a list of rows
            for i in range(col):  # Iterate over each row
                val[i] = {df.columns[j]: df_data[i][j] for j in range(row)}  # Create a dictionary for each row
            maptypeData.append([ky, val])  # Append the key and value to the map type data list
            df_map = spark.createDataFrame(maptypeData, mapSchema)  # Create a Spark DataFrame from the map type data
            
        df_map.write.format('delta').option('overwrite', True).mode('append').saveAsTable('multiSheetexcel')  # Write the DataFrame to a Delta table

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists multisheetexcel
