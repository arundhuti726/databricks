# 📊 Excel Metadata Extractor using Databricks & PySpark

## 🔍 Purpose

This project provides a robust, dynamic solution for extracting data and metadata from Excel files—regardless of schema or number of sheets—and storing them in Delta format using Databricks and PySpark. It is designed to consolidate all file-level and sheet-level details into a **single metadata table**, enabling centralized tracking, auditing, and downstream analysis.

By organizing file content alongside metadata such as file name, sheet name, modification time, and load timestamp, this solution helps:
- Maintain a **complete inventory of Excel data ingested over time**
- Enable **audit trails and data lineage tracking**
- Allow **query-based validation or monitoring** of file changes
- Serve as a **reference hub** for data quality checks or ingestion history
- Support integration with **dashboards or alerting systems** for failed/missing loads

This utility is especially useful when working with dynamic Excel file drops that may have varying structures or multiple sheets.

---

## ⚙️ Key Features

- 📁 **Dynamic Source Directory Selection**:  
  Utilizes a Databricks widget to let users select the folder path where the Excel files are stored at runtime.

- 📑 **Multi-Sheet Excel Handling**:  
  Automatically detects and reads **all sheets** from each Excel file without hardcoding sheet names.

- 🔄 **Schema Agnostic**:  
  Capable of handling Excel sheets with varying structures (column names, data types, etc.).

- 🧾 **Metadata Capturing**:  
  The output Delta table includes the following for each Excel sheet:
  - File name
  - Sheet name
  - Last modified time
  - Load timestamp
  - Flattened data content (rows from the sheet)

- 💾 **Delta Format Output**:  
  Data and metadata are written to a centralized Delta table for scalable querying and downstream processing.

---

## 🧠 How It Works

1. **User Input**  
   A widget allows users to provide the source directory path where Excel files are stored.

2. **File & Sheet Iteration**  
   - The script recursively lists all Excel files in the given location.
   - For each Excel file, all sheet names are extracted.
   - Each sheet is read dynamically into a DataFrame.

3. **Metadata Enrichment**  
   - Each DataFrame is augmented with metadata columns:
     - `file_name`
     - `sheet_name`
     - `last_modified_time`
     - `load_timestamp`

4. **Unified Write**  
   - All data is appended to a Delta table for persistent storage and audit purposes.

---

## 📁 Output Table Example

| file_name         | sheet_name | last_modified_time     | load_timestamp        | col1 | col2 | ... |
|------------------|-------------|-------------------------|------------------------|------|------|-----|
| `Report_June.xlsx` | `Sheet1`   | `2024-06-12 10:14:55`   | `2024-06-13 08:22:11`  | ...  | ...  | ... |
| `Report_June.xlsx` | `Sheet2`   | `2024-06-12 10:14:55`   | `2024-06-13 08:22:11`  | ...  | ...  | ... |
| `Report_July.xlsx` | `Summary`  | `2024-07-01 14:03:29`   | `2024-07-02 07:50:03`  | ...  | ...  | ... |

---

## 🚀 Technologies Used

- **Azure Databricks**
- **PySpark**
- **Databricks Widgets**
- **Delta Lake**

---

## 📌 Use Cases

- Audit tracking of Excel file ingestion
- Automated data lineage
- Monitoring changes in source Excel data
- Historical tracking of input files in a governed, queryable format

---

## 📣 Notes

- This utility assumes the Excel files are compatible with Spark's Excel reading capabilities (i.e., `.xlsx`)
- Schema may vary between sheets and files; the script handles this dynamically
- Ensure the appropriate Spark Excel libraries (`com.crealytics:spark-excel`) are available in your Databricks environment

---

