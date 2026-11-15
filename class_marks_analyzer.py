# Class Marks Analyzer
# This program analyzes marks for all students in a class.


def get_valid_count():
    # Ask for a positive whole number of students.
    while True:
        value = input("How many students are in the class? ").strip()
        try:
            count = int(value)
            if count > 0:
                return count
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_valid_mark(student_name):
    # Keep asking until the student's mark is a whole number from 0 to 100.
    while True:
        value = input(f"Enter marks for {student_name} (0-100): ").strip()
        try:
            mark = int(value)
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_students_with_mark(names, marks, target):
    # Display every student whose mark matches the target mark.
    for name, mark in zip(names, marks):
        if mark == target:
            print(f"{name}: {mark}")


def display_above_average(names, marks, average):
    # Display students whose marks are greater than the class average.
    found = False
    for name, mark in zip(names, marks):
        if mark > average:
            print(f"{name}: {mark}")
            found = True
    if not found:
        print("No students scored above the class average.")


def main():
    # Collect class data and display the required performance statistics.
    student_names = []
    student_marks = []

    count = get_valid_count()

    for number in range(1, count + 1):
        print(f"\nStudent {number}")
        name = input("Enter student name: ").strip().title()
        while not name:
            print("Name cannot be empty.")
            name = input("Enter student name: ").strip().title()

        mark = get_valid_mark(name)
        student_names.append(name)
        student_marks.append(mark)

    average = sum(student_marks) / len(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)

    passing = sum(1 for mark in student_marks if mark >= 50)
    failing = sum(1 for mark in student_marks if mark < 50)

    print("\n" + "=" * 42)
    print("            CLASS MARKS REPORT")
    print("=" * 42)
    print(f"Number of students : {len(student_names)}")
    print(f"Class average      : {average:.2f}")
    print(f"Highest marks      : {highest}")
    display_students_with_mark(student_names, student_marks, highest)
    print(f"Lowest marks       : {lowest}")
    display_students_with_mark(student_names, student_marks, lowest)
    print(f"Passing students  : {passing}")
    print(f"Failing students  : {failing}")

    print("\nStudents above class average:")
    display_above_average(student_names, student_marks, average)

    print("\nMarks from highest to lowest:")
    print(sorted(student_marks, reverse=True))
    print("=" * 42)


if __name__ == "__main__":
    main()
