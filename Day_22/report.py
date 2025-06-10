# Student Marks Report Card
students_data = []

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total, marks):
    return total / len(marks)

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    subjects = []
    marks = []
    
    # Get the number of subjects from the user
    num_subjects = int(input("How many subjects does the student have? "))
    
    for i in range(1, num_subjects + 1):
        subject_name = input(f"Enter name for subject {i}: ")
        subjects.append(subject_name)
        while True:
            try:
                mark = float(input(f"Enter marks for {subject_name} (out of 100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except:
                print("Enter a valid number.")
    
    total = calculate_total(marks)
    percentage = calculate_percentage(total,marks)
    grade = assign_grade(percentage)

    student_report = {
        'Name': name,
        'Subjects': subjects,
        'Marks': marks,
        'Total': total,
        'Percentage': round(percentage, 2),
        'Grade': grade
    }

    students_data.append(student_report)
    print(f"\n{name}'s Report: Total = {total}, Percentage = {percentage:.2f}%, Grade = {grade}\n")

def display_reports():
    if not students_data:
        print("No student data available.")
        return
    print("\n=== All Students Report ===")
    for student in students_data:
        print(f"\nName: {student['Name']}")
        for i in range(len(student['Subjects'])):
            print(f"{student['Subjects'][i]}: {student['Marks'][i]}")
        print(f"Total: {student['Total']}")
        print(f"Percentage: {student['Percentage']}%")
        print(f"Grade: {student['Grade']}")

def student_grader():
    while True:
        print("\n--- Student Marks Grader ---")
        print("1. Add Student")
        print("2. Show All Reports")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_reports()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Start the program
student_grader()
