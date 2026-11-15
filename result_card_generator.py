# Student Result Card Generator
# This program collects one student's details and prints a result card.

SUBJECTS = ["English", "Mathematics", "Science", "Computer", "Urdu"]


def format_name(name):
    # Remove extra spaces and capitalize each part of the student's name.
    return name.strip().title()


def get_valid_marks(subject):
    # Keep asking until the user enters a whole-number mark from 0 to 100.
    while True:
        value = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            marks = int(value)
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks. Enter a number from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_percentage(total, max_total):
    # Calculate the percentage and return it.
    return (total / max_total) * 100


def get_grade(percentage):
    # Return the letter grade according to the given grading scale.
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
    return "Fail"


def get_valid_roll_number():
    # Accept a roll number only when it contains digits.
    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            return roll_number
        print("Invalid roll number. Use digits only.")


def main():
    # Collect student information, calculate the result, and display the card.
    print("\nSTUDENT RESULT CARD")
    print("-------------------")

    name = format_name(input("Enter student name: "))
    while not name:
        print("Name cannot be empty.")
        name = format_name(input("Enter student name: "))

    roll_number = get_valid_roll_number()

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_valid_marks(subject)

    total = sum(marks.values())
    max_total = len(SUBJECTS) * 100
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)

    # A mark below 40 in any subject means the student fails overall.
    if any(mark < 40 for mark in marks.values()):
        status = "Fail"
    else:
        status = "Pass"

    print("\n" + "=" * 38)
    print("             RESULT CARD")
    print("=" * 38)
    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll_number}")
    print("-" * 38)
    for subject, mark in marks.items():
        print(f"{subject:<16}: {mark:>3}/100")
    print("-" * 38)
    print(f"Total Marks  : {total}/{max_total}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Letter Grade : {grade}")
    print(f"Final Status : {status}")
    print("=" * 38)


if __name__ == "__main__":
    main()
