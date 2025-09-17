# Same Student Grade Calculator - CLEAN VERSION (with functions)

def get_valid_score(test_name):
    """Get a valid test score (0-100) from user input."""
    while True:
        score = input(f"{test_name}: ")
        if score.isdigit() and 0 <= int(score) <= 100:
            return int(score)
        print("Invalid input! Please enter a number between 0 and 100.")


def calculate_letter_grade(average):
    """Convert a numeric average to a letter grade."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_student_scores():
    """Get all three test scores for a student."""
    print("Enter test scores (0-100):")
    test1 = get_valid_score("Test 1")
    test2 = get_valid_score("Test 2")
    test3 = get_valid_score("Test 3")
    return test1, test2, test3


def calculate_average(scores):
    """Calculate the average of test scores."""
    return sum(scores) / len(scores)


def process_student(student_number):
    """Process one complete student: get name, scores, calculate grades."""
    print(f"Enter grades for Student {student_number}:")
    name = input("Student name: ")

    scores = get_student_scores()
    average = calculate_average(scores)
    letter_grade = calculate_letter_grade(average)

    return {
        'name': name,
        'scores': scores,
        'average': average,
        'letter_grade': letter_grade
    }


def display_student_results(student_data):
    """Display formatted results for one student."""
    name = student_data['name']
    scores = student_data['scores']
    average = student_data['average']
    letter_grade = student_data['letter_grade']

    print(f"\n--- {name}'s Results ---")
    print(f"Test Scores: {', '.join(map(str, scores))}")
    print(f"Average: {average:.1f}")
    print(f"Letter Grade: {letter_grade}")


def display_class_summary(students):
    """Display summary statistics for the entire class."""
    print("\n=== CLASS SUMMARY ===")

    class_average = sum(student['average'] for student in students) / len(students)
    print(f"Class Average: {class_average:.1f}")

    print("Individual Averages:")
    for student in students:
        print(f"  {student['name']}: {student['average']:.1f} ({student['letter_grade']})")


def main():
    """Main program function."""
    print("=== STUDENT GRADE CALCULATOR ===")
    print()

    # Process all students
    students = []
    for i in range(1, 4):  # Students 1, 2, 3
        student_data = process_student(i)
        display_student_results(student_data)
        students.append(student_data)
        print()

    # Show class summary
    display_class_summary(students)


# Run the program
if __name__ == "__main__":
    main()
