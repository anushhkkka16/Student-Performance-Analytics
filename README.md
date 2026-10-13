# Student Performance Analytics System

## 1. Project Overview
The Student Performance Analytics System is a Python-based project that analyses student marks and attendance. It uses Pandas and NumPy to calculate results and generate useful summaries.

## 2. Objectives
- Analyse student marks in different subjects.
- Calculate total marks and average scores.
- Assign grades and determine pass or fail status.
- Identify the top five students.
- Analyse attendance eligibility.
- Identify subject-wise toppers.
- Generate a CSV file containing student results.

## 3. Technologies Used
- **Python:** Main programming language.
- **Pandas:** Data handling and analysis.
- **NumPy:** Numerical calculations and conditional operations.
- **CSV:** Storage of student data and results.

## 4. Dataset
The project uses a CSV dataset containing 20 fictional student records. Each record includes a student ID, name, department, marks in Mathematics, Science and English, and attendance percentage.

## 5. Features
1. Calculates total marks and average scores.
2. Assigns grades based on average marks.
3. Displays pass or fail status.
4. Calculates class and subject averages.
5. Identifies the highest and lowest student averages.
6. Displays the top five students.
7. Checks attendance eligibility using a 75% threshold.
8. Identifies the topper in each subject.
9. Saves processed results to `student_results.csv`.

## 6. How to Run
1. Install Python.
2. Install the required libraries using:

   `py -m pip install pandas numpy`

3. Place `main.py` and `students.csv` in the same folder.
4. Open Command Prompt in that folder.
5. Run:

   `py main.py`

## 7. Output
The program displays student results, class statistics, subject averages, attendance information, the top five students and subject-wise toppers. It also generates `student_results.csv`.

## 8. Conclusion
This project demonstrates how Python, Pandas and NumPy can be used to organise student data, perform basic analysis and produce meaningful academic summaries.
