"""Analyze marks and performance statistics for a class."""

MIN_MARKS = 0
MAX_MARKS = 100
PASS_MARK = 50


def get_positive_integer(prompt):
    """Read a positive whole number."""
    while True:
        raw_value = input(prompt).strip()
        try:
            number = int(raw_value)
        except ValueError:
            print("Error: enter a valid whole number.")
            continue
        if number > 0:
            return number
        print("Error: value must be greater than zero.")


def get_non_empty_name(prompt):
    """Read a non-empty name and normalize its capitalization."""
    while True:
        name = input(prompt).strip()
        if name:
            return name.title()
        print("Error: student name cannot be blank.")


def get_mark(name):
    """Read one whole-number mark in the inclusive 0-100 range."""
    while True:
        raw_value = input(f"Enter marks for {name} (0-100): ").strip()
        try:
            mark = int(raw_value)
        except ValueError:
            print("Error: enter a whole number from 0 to 100.")
            continue
        if MIN_MARKS <= mark <= MAX_MARKS:
            return mark
        print("Error: marks must be between 0 and 100.")


def collect_students():
    """Collect each student's name and mark into a list of dictionaries."""
    count = get_positive_integer("How many students are in the class? ")
    students = []
    for index in range(count):
        print(f"\nStudent {index + 1}")
        name = get_non_empty_name("Enter student name: ")
        mark = get_mark(name)
        students.append({"name": name, "mark": mark})
    return students


def calculate_statistics(students):
    """Return class average, extrema, pass/fail counts, and ordered marks."""
    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passing_count": sum(mark >= PASS_MARK for mark in marks),
        "failing_count": sum(mark < PASS_MARK for mark in marks),
        "above_average": [
            student for student in students if student["mark"] > average
        ],
        "sorted_marks": sorted(marks, reverse=True),
    }


def display_analysis(students, statistics):
    """Print the class performance report."""
    print("\n" + "=" * 38)
    print("          CLASS MARKS ANALYSIS")
    print("=" * 38)
    print(f"Number of students : {len(students)}")
    print(f"Class average      : {statistics['average']:.2f}")
    print(f"Highest marks      : {statistics['highest']}")
    for student in students:
        if student["mark"] == statistics["highest"]:
            print(f"{student['name']}: {student['mark']}")
    print(f"Lowest marks       : {statistics['lowest']}")
    for student in students:
        if student["mark"] == statistics["lowest"]:
            print(f"{student['name']}: {student['mark']}")
    print(f"Passing students   : {statistics['passing_count']}")
    print(f"Failing students   : {statistics['failing_count']}")
    print("Students above class average:")
    if statistics["above_average"]:
        for student in statistics["above_average"]:
            print(f"{student['name']}: {student['mark']}")
    else:
        print("None")
    print("Marks from highest to lowest:")
    print(statistics["sorted_marks"])
    print("=" * 38)


def main():
    """Collect class data, calculate statistics, and display the report."""
    print("Class Marks Analyzer")
    students = collect_students()
    statistics = calculate_statistics(students)
    display_analysis(students, statistics)


if __name__ == "__main__":
    main()
