import os
import random
import pandas as pd
import json
import numpy as np
import logging
import matplotlib.pyplot as plt
from datetime import datetime

#Creating Log File
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("Data/output/process_log.txt"),
        logging.StreamHandler()
    ]
)

logging.info("Process started")

#Creating dicts
try:
    os.makedirs('Data/raw', exist_ok=True)
    os.makedirs('Data/clean', exist_ok=True)
    os.makedirs('Data/output', exist_ok=True)
    logging.info("Dicts created")
except Exception as e:
    logging.error(f"Error creating dicts: {e}")

#Generating synthetic student data
try:
    names = [
        "Ali", "John", "Sarah", "Maya", "David",
        "Lina", "James", "Sophia", "Daniel", "Emma"
    ]

    cities = [
        "Beirut", "Dubai", "Doha", "Mumbai", "London"
    ]

    genders = ["Male", "Female"]

    students = []

    for i in range(1, 201):
        student = {
            "id": i,
            "name": random.choice(names),
            "age": random.choice([random.randint(17, 25), None]),
            "gender": random.choice(genders),
            "marks": random.randint(-10, 110),
            "attendance": random.randint(-10, 110),
            "city": random.choice(cities + [None])
        }

        students.append(student)

    with open('Data/raw/raw_students.json', 'w') as f:
        json.dump(students, f, indent=4)

    logging.info("Synthetic student data generated")

except Exception as e:
    logging.error(f"Error generating student data: {e}")

#Reading the json File
df = None

try:
    df = pd.read_json('Data/raw/raw_students.json')
    logging.info("JSON file loaded")
except Exception as e:
    logging.error(f"Error loading JSON: {e}")

#Cleaning & Validation
if df is not None:

    try:
        df = df[(df['marks'] >= 0) & (df['marks'] <= 100)]
        df = df[(df['attendance'] >= 0) & (df['attendance'] <= 100)]

        df['age'].fillna(df['age'].mean(), inplace=True)
        df['city'].fillna('Unknown', inplace=True)

        df['gender'] = df['gender'].replace({
            'Male': 'M',
            'Female': 'F'
        })

        csv_path = 'Data/clean/clean_students.csv'
        df.to_csv(csv_path, index=False)

        logging.info("Cleaning completed")

    except Exception as e:
        logging.error(f"Error during cleaning: {e}")

#transformation
    try:
        df = pd.read_csv(csv_path)

        df['pass_fail'] = df['marks'].apply(
            lambda x: 'Pass' if x >= 40 else 'Fail'
        )

        df['grade'] = df['marks'].apply(
            lambda x: 'A' if 90 <= x <= 100 else
                      'B' if 75 <= x <= 89 else
                      'C' if 60 <= x <= 74 else
                      'D' if 40 <= x <= 59 else 'F'
        )

        logging.info("Transformation completed")

    except Exception as e:
        logging.error(f"Error transforming data: {e}")

#Generating parquet file
    try:
        df.to_parquet(
            'Data/clean/clean_students.parquet',
            index=False
        )

        logging.info("Parquet file generated")

    except Exception as e:
        logging.error(f"Error saving Parquet: {e}")

#Matrix Multi analysis
    try:
        A = np.random.randint(1, 100, (500, 500))
        B = np.random.randint(1, 100, (500, 500))

        C = A @ B

        row_sums = np.sum(C, axis=1)

        matrix_output_path = 'Data/output/matrix_results.txt'

        np.savetxt(
            matrix_output_path,
            row_sums,
            fmt='%.2f',
            header='Row Sums'
        )

        logging.info("Matrix multiplication completed")

    except Exception as e:
        logging.error(f"Error in matrix operations: {e}")

#plotting
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(df['marks'], bins=15)
        plt.title('Distribution of Marks')
        plt.xlabel('Marks')
        plt.ylabel('Frequency')

        plt.savefig('Data/output/marks_distribution.png')
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.scatter(df['attendance'], df['marks'])

        plt.title('Attendance vs Marks Correlation')
        plt.xlabel('Attendance')
        plt.ylabel('Marks')

        plt.savefig('Data/output/attendance_marks_correlation.png')
        plt.close()

        logging.info("Plots generated")

    except Exception as e:
        logging.error(f"Error saving plots: {e}")

#summary
    try:
        avg_marks_per_city = df.groupby('city')['marks'].mean().to_dict()

        grade_a_percentage = (
            df['grade'].value_counts(normalize=True).get('A', 0)
        ) * 100

        top_city_attendance = (
            df.groupby('city')['attendance'].mean().idxmax()
        )

        summary = {
            "average_marks_per_city": avg_marks_per_city,
            "percentage_A_grade_students": grade_a_percentage,
            "city_with_highest_average_attendance": top_city_attendance
        }

        with open('Data/output/summary_report.json', 'w') as f:
            json.dump(summary, f, indent=4)

        logging.info("Summary report JSON written successfully")

    except Exception as e:
        logging.error(f"Error saving summary: {e}")

else:
    logging.error(
        "Process aborted: df is not defined because JSON failed to load."
    )

logging.info("Process completed")

print("ETL Pipeline completed successfully")