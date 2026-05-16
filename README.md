# Student ETL Pipeline

## Overview

This project is a Python-based ETL (Extract, Transform, Load) pipeline that generates synthetic student data, performs data cleaning and validation, transforms and analyzes the data using Pandas and NumPy, creates visualizations, performs matrix operations, and exports the processed data into multiple formats including CSV, JSON, TXT, and Parquet.

The project demonstrates:

* Data generation
* Data cleaning
* Data transformation
* Data analysis
* Matrix operations
* Data visualization
* Logging and exception handling
* Complete ETL workflow automation

---

## Features

* Generate 200 synthetic student records
* Save raw data as JSON
* Clean and validate records
* Replace missing values
* Convert gender values
* Generate grades and pass/fail status
* Perform aggregations and analytics
* Generate plots using Matplotlib
* Perform NumPy matrix multiplication
* Export CSV and Parquet files
* Logging with timestamps
* Automated ETL pipeline

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* JSON
* Parquet

---

## Project Structure

```bash id="r8m2qa"
Student-ETL-Pipeline/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── etl_pipeline.py
│
├── Data/
│   ├── raw/
│   │   └── raw_students.json
│   │
│   ├── clean/
│   │   ├── clean_students.csv
│   │   └── clean_students.parquet
│   │
│   └── output/
│       ├── summary_report.json
│       ├── matrix_results.txt
│       ├── marks_distribution.png
│       ├── attendance_marks_correlation.png
│       └── process_log.txt
│
└── screenshots/
```

---

## How to Run the Project

1. Install Python

2. Install required libraries:

```bash id="u3k9vl"
pip install pandas numpy matplotlib pyarrow
```

3. Put all project files in the same folder.

4. Run:

```bash id="f6w1xp"
python etl_pipeline.py
```

5. The pipeline will automatically:

* Generate synthetic student data
* Clean and validate records
* Transform the data
* Generate reports and plots
* Save CSV, JSON, TXT, and Parquet files

---

## Outputs Generated

* raw_students.json
* clean_students.csv
* clean_students.parquet
* summary_report.json
* matrix_results.txt
* marks_distribution.png
* attendance_marks_correlation.png
* process_log.txt

---

## Author

Tarek Rajab

---

## License

This project is licensed under the MIT License.
