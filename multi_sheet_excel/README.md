# 📊 Excel & CSV Metadata Extractor using Databricks & PySpark

## 🔍 Purpose

This project provides a robust, dynamic solution for extracting both data and metadata from **Excel and CSV files**, regardless of their schema or structure. Built in **Databricks using PySpark**, it captures essential metadata and content from all sheets (in Excel) or records (in CSV), and stores them in **Delta format**.

The main goal is to consolidate file-level and sheet-level metadata into a **single Delta table**, enabling centralized tracking, auditing, and downstream analytics.

By organizing file content alongside metadata such as file name, sheet name (for Excel), modification time, and load timestamp, this solution helps:
- Maintain a **complete inventory of all ingested Excel/CSV files**
- Enable **audit trails and ingestion history**
- Support **query-based validation or alerts** for missing or incorrect data
- Serve as a **metadata reference hub** across projects

---

## ⚙️ Key Features

- 📁 **Dynamic Source Directory Selection**  
  A Databricks widget allows users to select the input folder at runtime.

- 📑 **Multi-Sheet Excel Handling**  
  Automatically detects and reads all sheets from `.xlsx` files.

- 📄 **CSV Support**  
  Reads and processes CSV files seamlessly, with schema inferred dynamically.

- 🔄 **Schema Agnostic**  
  Handles varying structures across files and sheets.

- 🧾 **Metadata Capturing**  
  Each record written to the Delta table includes:
  - `file_name`
  - `sheet_name` (null for CSV)
  - `file_type` (Excel / CSV)
  - `last_modified_time`
  - `load_timestamp`
  - Data columns (schema varies per file)

- 💾 **Delta Format Output**  
  All content and metadata is appended to a Delta table for scalable querying.

---

## 🧠 How It Works

1. **User Input**  
   A Databricks widget is used to provide the **source directory path**.

2. **File Scanning**  
   - The script scans the folder for `.xlsx` and `.csv` files.
   - For Excel files: it reads **all sheets**.
   - For CSV files: it reads the file as a flat table.

3. **Metadata Enrichment**  
   - Each record is tagged with:
     - `file_name`
     - `sheet_name` (Excel only)
     - `file_type` (Excel/CSV)
     - `last_modified_time`
     - `load_timestamp`

4. **Unified Write to Delta**  
   - All extracted data and metadata are saved into a single Delta table.

---

## 📁 Output Table Example

| file_name         | sheet_name | file_type | last_modified_time     | load_timestamp        | col1 | col2 | ... |
|------------------|-------------|------------|-------------------------|------------------------|------|------|-----|
| `Sales_Q2.xlsx`   | `Sheet1`    | Excel      | `2024-06-12 10:14:55`   | `2024-06-13 08:22:11`  | ...  | ...  | ... |
| `Sales_Q2.xlsx`   | `Sheet2`    | Excel      | `2024-06-12 10:14:55`   | `2024-06-13 08:22:11`  | ...  | ...  | ... |
| `customers.csv`   | `null`      | CSV        | `2024-07-01 09:45:29`   | `2024-07-01 09:47:03`  | ...  | ...  | ... |

---

## 🚀 Technologies Used

- **Azure Databricks**
- **PySpark**
- **Databricks Widgets**
- **Delta Lake**
- **crealytics Spark Excel Library** (for `.xlsx` support)

---

## 📌 Use Cases

- Tracking and managing ingestion of CSV and Excel files
- Centralized data quality checks and validation logic
- Historical data change tracking and reporting
- Metadata lineage and compliance logging
- Input layer for data catalogs or dashboards

---

## 📣 Notes

- Ensure the **Spark Excel package** (`com.crealytics:spark-excel_2.12`) is installed in your Databricks cluster.
- The script supports `.xlsx` and `.csv` files only.
- The output Delta table is append-mode and can be queried for auditing or alerting purposes.

