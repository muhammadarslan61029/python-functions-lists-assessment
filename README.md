# Python Functions and Lists Assessment

## Project Overview

This project contains two separate Python programs for a training institute:

1. **Student Result Card Generator** — collects one student's details and marks in five subjects, checks the input, calculates the percentage and grade, and prints a formatted result card.
2. **Class Marks Analyzer** — collects names and marks for a class, then calculates class performance statistics.

## Files

- `result_card_generator.py` — the individual student result card program.
- `class_marks_analyzer.py` — the class performance analysis program.

## Python Concepts Used

- Functions using `def`, parameters, and `return`
- String methods: `strip()`, `title()`, and `isdigit()`
- Lists and dictionaries
- `append()`, `len()`, `sum()`, `max()`, `min()`, and `sorted()`
- Loops and conditional statements
- Input validation and `try` / `except`
- List comprehensions / generator expressions
- f-strings for formatted output

## Requirements

- Python 3 installed on your computer.
- No external libraries are required.

## How to Run

Open a terminal in this project folder.

Run the result card program:

```bash
python result_card_generator.py
```

Run the class analyzer:

```bash
python class_marks_analyzer.py
```

On some systems, use `python3` instead of `python`.

## Sample Input and Output

### 1. Student Result Card Generator

Example input:

```text
Enter student name:  ali raza
Enter roll number: 61016
Enter marks for English (0-100): 85
Enter marks for Mathematics (0-100): 92
Enter marks for Science (0-100): 78
Enter marks for Computer (0-100): 88
Enter marks for Urdu (0-100): 81
```

Example output (main result):

```text
Student Name : Ali Raza
Roll Number  : 61016
English         :  85/100
Mathematics     :  92/100
Science         :  78/100
Computer        :  88/100
Urdu            :  81/100
Total Marks  : 424/500
Percentage   : 84.80%
Letter Grade : A
Final Status : Pass
```

### 2. Class Marks Analyzer

Example input:

```text
How many students are in the class? 3

Student 1
Enter student name: Ali
Enter marks for Ali (0-100): 80

Student 2
Enter student name: Sara
Enter marks for Sara (0-100): 45

Student 3
Enter student name: Ahmed
Enter marks for Ahmed (0-100): 95
```

Example output (main results):

```text
Number of students : 3
Class average      : 73.33
Highest marks      : 95
Ahmed: 95
Lowest marks       : 45
Sara: 45
Passing students  : 2
Failing students  : 1

Students above class average:
Ali: 80
Ahmed: 95

Marks from highest to lowest:
[95, 80, 45]
```

## Notes

- In the result card program, a student fails if at least one subject mark is below 40, even if the overall percentage is high.
- The grade is calculated from the overall percentage using the assessment's grading scale.
- In the class analyzer, passing means a mark of 50 or above.
- Both programs reject invalid marks and ask the user to enter them again.
