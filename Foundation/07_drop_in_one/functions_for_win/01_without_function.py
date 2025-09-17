# Student Grade Calculator - MESSY VERSION (no functions)
print("=== STUDENT GRADE CALCULATOR ===")
print()

# Student 1
print("Enter grades for Student 1:")
student1_name = input("Student name: ")

# Get Student 1's test scores
print("Enter test scores (0-100):")
student1_test1 = input("Test 1: ")
while not student1_test1.isdigit() or int(student1_test1) < 0 or int(student1_test1) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student1_test1 = input("Test 1: ")
student1_test1 = int(student1_test1)

student1_test2 = input("Test 2: ")
while not student1_test2.isdigit() or int(student1_test2) < 0 or int(student1_test2) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student1_test2 = input("Test 2: ")
student1_test2 = int(student1_test2)

student1_test3 = input("Test 3: ")
while not student1_test3.isdigit() or int(student1_test3) < 0 or int(student1_test3) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student1_test3 = input("Test 3: ")
student1_test3 = int(student1_test3)

# Calculate Student 1's average
student1_average = (student1_test1 + student1_test2 + student1_test3) / 3

# Determine Student 1's letter grade
if student1_average >= 90:
    student1_letter = "A"
elif student1_average >= 80:
    student1_letter = "B"
elif student1_average >= 70:
    student1_letter = "C"
elif student1_average >= 60:
    student1_letter = "D"
else:
    student1_letter = "F"

print(f"\n--- {student1_name}'s Results ---")
print(f"Test Scores: {student1_test1}, {student1_test2}, {student1_test3}")
print(f"Average: {student1_average:.1f}")
print(f"Letter Grade: {student1_letter}")
print()

# Student 2 (EXACT SAME CODE REPEATED!)
print("Enter grades for Student 2:")
student2_name = input("Student name: ")

# Get Student 2's test scores
print("Enter test scores (0-100):")
student2_test1 = input("Test 1: ")
while not student2_test1.isdigit() or int(student2_test1) < 0 or int(student2_test1) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student2_test1 = input("Test 1: ")
student2_test1 = int(student2_test1)

student2_test2 = input("Test 2: ")
while not student2_test2.isdigit() or int(student2_test2) < 0 or int(student2_test2) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student2_test2 = input("Test 2: ")
student2_test2 = int(student2_test2)

student2_test3 = input("Test 3: ")
while not student2_test3.isdigit() or int(student2_test3) < 0 or int(student2_test3) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student2_test3 = input("Test 3: ")
student2_test3 = int(student2_test3)

# Calculate Student 2's average
student2_average = (student2_test1 + student2_test2 + student2_test3) / 3

# Determine Student 2's letter grade
if student2_average >= 90:
    student2_letter = "A"
elif student2_average >= 80:
    student2_letter = "B"
elif student2_average >= 70:
    student2_letter = "C"
elif student2_average >= 60:
    student2_letter = "D"
else:
    student2_letter = "F"

print(f"\n--- {student2_name}'s Results ---")
print(f"Test Scores: {student2_test1}, {student2_test2}, {student2_test3}")
print(f"Average: {student2_average:.1f}")
print(f"Letter Grade: {student2_letter}")
print()

# Student 3 (SAME CODE AGAIN!)
print("Enter grades for Student 3:")
student3_name = input("Student name: ")

# Get Student 3's test scores
print("Enter test scores (0-100):")
student3_test1 = input("Test 1: ")
while not student3_test1.isdigit() or int(student3_test1) < 0 or int(student3_test1) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student3_test1 = input("Test 1: ")
student3_test1 = int(student3_test1)

student3_test2 = input("Test 2: ")
while not student3_test2.isdigit() or int(student3_test2) < 0 or int(student3_test2) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student3_test2 = input("Test 2: ")
student3_test2 = int(student3_test2)

student3_test3 = input("Test 3: ")
while not student3_test3.isdigit() or int(student3_test3) < 0 or int(student3_test3) > 100:
    print("Invalid input! Please enter a number between 0 and 100.")
    student3_test3 = input("Test 3: ")
student3_test3 = int(student3_test3)

# Calculate Student 3's average
student3_average = (student3_test1 + student3_test2 + student3_test3) / 3

# Determine Student 3's letter grade
if student3_average >= 90:
    student3_letter = "A"
elif student3_average >= 80:
    student3_letter = "B"
elif student3_average >= 70:
    student3_letter = "C"
elif student3_average >= 60:
    student3_letter = "D"
else:
    student3_letter = "F"

print(f"\n--- {student3_name}'s Results ---")
print(f"Test Scores: {student3_test1}, {student3_test2}, {student3_test3}")
print(f"Average: {student3_average:.1f}")
print(f"Letter Grade: {student3_letter}")
print()

# Final summary
print("=== CLASS SUMMARY ===")
class_average = (student1_average + student2_average + student3_average) / 3
print(f"Class Average: {class_average:.1f}")
print("Individual Averages:")
print(f"  {student1_name}: {student1_average:.1f} ({student1_letter})")
print(f"  {student2_name}: {student2_average:.1f} ({student2_letter})")
print(f"  {student3_name}: {student3_average:.1f} ({student3_letter})")
