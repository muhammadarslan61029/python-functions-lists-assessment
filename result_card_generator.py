"""Generate a validated result card for one student."""

SUBJECTS = ("English", "Mathematics", "Science", "Computer", "Urdu")
MIN_MARKS = 0
MAX_MARKS = 100
SUBJECT_PASS_MARK = 40
GRADE_THRESHOLDS = ((80, "A"), (70, "B"), (60, "C"), (50, "D"), (0, "F"))


def get_non_empty_text(prompt):
    """Read text and reject blank values."""
    while True:
        value = input(prompt).strip()
        if value:
            return value.title()
        print("Error: this field cannot be blank.")


def get_roll_number():
    """Read a roll number containing digits only."""
    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            return roll_number
        print("Error: roll number must contain digits only.")


def get_mark(subject):
    """Read one whole-number mark in the inclusive 0-100 range."""
    while True:
        raw_value = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            mark = int(raw_value)
        except ValueError:
            print("Error: enter a whole number from 0 to 100.")
            continue
        if MIN_MARKS <= mark <= MAX_MARKS:
            return mark
        print("Error: marks must be between 0 and 100.")


def calculate_grade(percentage):
    """Return the letter grade for an overall percentage."""
    for threshold, grade in GRADE_THRESHOLDS:
        if percentage >= threshold:
            return grade
    return "F"


def build_result(name, roll_number, marks):
    """Calculate totals, percentage, grade, and final pass/fail status."""
    total = sum(marks.values())
    maximum_total = len(SUBJECTS) * MAX_MARKS
    percentage = total / maximum_total * 100
    grade = calculate_grade(percentage)
    passed = all(mark >= SUBJECT_PASS_MARK for mark in marks.values())
    return {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "total": total,
        "maximum_total": maximum_total,
        "percentage": percentage,
        "grade": grade,
        "status": "Pass" if passed else "Fail",
    }


def display_result(result):
    """Print the formatted student result card."""
    print("\n" + "=" * 34)
    print("           STUDENT RESULT CARD")
    print("=" * 34)
    print(f"Student Name : {result['name']}")
    print(f"Roll Number  : {result['roll_number']}")
    for subject, mark in result["marks"].items():
        print(f"{subject:<14}: {mark:>3}/100")
    print("-" * 34)
    print(f"Total Marks  : {result['total']}/{result['maximum_total']}")
    print(f"Percentage   : {result['percentage']:.2f}%")
    print(f"Letter Grade : {result['grade']}")
    print(f"Final Status : {result['status']}")
    print("=" * 34)


def main():
    """Collect student data and display the result card."""
    print("Student Result Card Generator")
    name = get_non_empty_text("Enter student name: ")
    roll_number = get_roll_number()
    marks = {subject: get_mark(subject) for subject in SUBJECTS}
    display_result(build_result(name, roll_number, marks))


if __name__ == "__main__":
    main()
