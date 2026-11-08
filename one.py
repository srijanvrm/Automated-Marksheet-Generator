
# Student Name          : SRIJAN
# ERP Number            : 00049
# Course                : BCA 1 B
# Programming Language  : Python 3
# Project Number        : PS No. 90
# Project Description   : Automated Marksheet Generator

import os
import pandas as pd

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "marks.csv"
)


def create_csv():
    if not os.path.exists(FILE_NAME):
        data = {
            "RollNo": [101, 102, 103, 104],
            "Name": ["Anita", "Rahul", "Suman", "Vikas"],
            "Maths": [85, 40, 35, 100],
            "Physics": [90, 45, 70, 100],
            "Programming": [80, 50, 60, 100]
        }

        df = pd.DataFrame(data)
        df.to_csv(FILE_NAME, index=False)

        print("Sample marks.csv file created!")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def generate_marksheet():

    create_csv()

    try:
        df = pd.read_csv(FILE_NAME)

    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("Error: Unable to read marks.csv!")
        return

    required = [
        "RollNo", "Name", "Maths",
        "Physics", "Programming"
    ]

    if not all(column in df.columns for column in required):
        print("Error: CSV columns are missing!")
        return

    subjects = ["Maths", "Physics", "Programming"]
    valid_students = []

    # Validate all student records
    for _, student in df.iterrows():

        roll_no = str(student["RollNo"]).strip()

        if roll_no.endswith(".0"):
            roll_no = roll_no[:-2]

        marks = []

        try:
            for subject in subjects:
                mark = pd.to_numeric(
                    student[subject],
                    errors="coerce"
                )

                if pd.isna(mark) or not 0 <= mark <= 100:
                    raise ValueError

                marks.append(float(mark))

        except (ValueError, TypeError):
            print(
                f"Warning: Row for roll {roll_no} skipped - "
                "marks must be between 0 and 100."
            )
            continue

        valid_students.append({
            "RollNo": roll_no,
            "Name": student["Name"],
            "Maths": marks[0],
            "Physics": marks[1],
            "Programming": marks[2]
        })

    roll_no = input("Enter Roll Number: ").strip()

    student = None

    for s in valid_students:
        if s["RollNo"] == roll_no:
            student = s
            break

    if student is None:
        print(f"Roll number {roll_no} not found.")
        return

    marks = [
        student["Maths"],
        student["Physics"],
        student["Programming"]
    ]

    total = sum(marks)
    percentage = (total / 300) * 100
    grade = calculate_grade(percentage)

    failed_subjects = [
        subject
        for subject, mark in zip(subjects, marks)
        if mark < 40
    ]

    if failed_subjects:
        result = f"FAIL ({', '.join(failed_subjects)} below 40)"
    else:
        result = "PASS"

    print("\n========== STUDENT MARKSHEET ==========")

    print(f"Roll No: {roll_no} | Name: {student['Name']}")

    print(
        f"Maths: {marks[0]:g} | "
        f"Physics: {marks[1]:g} | "
        f"Programming: {marks[2]:g}"
    )

    print(f"Total: {total:g}/300 | Percentage: {percentage:.2f}%")
    print(f"Grade: {grade} | Result: {result}")

    print("=======================================")


if __name__ == "__main__":
    generate_marksheet()
