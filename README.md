# Automated Marksheet Generator

A Python 3 application that reads student marks from a CSV file, calculates total marks and percentage, assigns a grade, and displays whether the student has passed or failed.

## Project Details

| Field | Details |
|---|---|
| Student Name | SRIJAN |
| ERP Number | 00049 |
| Course | BCA 1 B |
| Project Number | PS No. 90 |
| Programming Language | Python 3 |

## Features

- Reads student records from `marks.csv` using Pandas.
- Searches for a student using their roll number.
- Validates that each subject mark is between 0 and 100.
- Skips records containing invalid marks and displays a warning.
- Calculates total marks out of 300 and percentage.
- Assigns a grade based on the percentage.
- Displays PASS or FAIL. A student must score at least 40 in each subject to pass.

## Grade Criteria

| Percentage | Grade |
|---|---|
| 90% and above | A+ |
| 80% to below 90% | A |
| 70% to below 80% | B |
| 60% to below 70% | C |
| 50% to below 60% | D |
| 40% to below 50% | E |
| Below 40% | F |

## Requirements

- Python 3
- Pandas

## Installation

Install Pandas:

```bash
python -m pip install pandas
```

## Project Files

- `one.py` – Main Python program.
- `marks.csv` – Student marks data.
- `README.md` – Project documentation.
- `Test_cases_passed.pdf` – Test-case report.
- `PS_No_90_Project_Details.png` – Project allocation screenshot.

## CSV Format

The CSV file must contain these column headings:

```text
RollNo,Name,Maths,Physics,Programming
```

## How to Run

1. Keep `one.py` and `marks.csv` in the same folder.
2. Open a terminal in that folder.
3. Run:

```bash
python one.py
```

4. Enter the student's roll number when prompted.

## Result Calculation

- Total = Maths + Physics + Programming
- Percentage = (Total / 300) × 100
- PASS requires at least 40 marks in every subject; otherwise, the result is FAIL.

---
**Project:** Automated Marksheet Generator  
**PS No.:** 90
