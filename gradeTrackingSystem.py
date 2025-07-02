def get_letter_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def main():
    students = {}

    while True:
        print("\nGrade Tracking System")
        print("1. Add student and grade")
        print("2. View all students and grades")
        print("3. Update a student's grade")
        print("4. Remove a student")
        print("5. View average grade")
        print("6. View highest and lowest grade")
        print("7. Count total students")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter student name: ")
            if name in students:
                print("Student already exists.")
            else:
                try:
                    grade = float(input("Enter grade (0-100): "))
                    if 0 <= grade <= 100:
                        students[name] = grade
                        print(f"{name}'s grade added.")
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid grade input.")

        elif choice == '2':
            if students:
                print("\nStudent Grades:")
                for name, grade in students.items():
                    letter = get_letter_grade(grade)
                    print(f"{name}: {grade} → {letter}")
            else:
                print("No student records found.")

        elif choice == '3':
            name = input("Enter student name to update: ")
            if name in students:
                try:
                    new_grade = float(input("Enter new grade: "))
                    if 0 <= new_grade <= 100:
                        students[name] = new_grade
                        print(f"{name}'s grade updated.")
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid grade input.")
            else:
                print("Student not found.")

        elif choice == '4':
            name = input("Enter student name to remove: ")
            if name in students:
                del students[name]
                print(f"{name} removed.")
            else:
                print("Student not found.")

        elif choice == '5':
            if students:
                avg = sum(students.values()) / len(students)
                avg_letter = get_letter_grade(avg)
                print(f"Average grade: {avg:.2f} → {avg_letter}")
            else:
                print("No grades available to calculate average.")

        elif choice == '6':
            if students:
                highest = max(students.values())
                lowest = min(students.values())
                high_letter = get_letter_grade(highest)
                low_letter = get_letter_grade(lowest)
                print(f"Highest grade: {highest} → {high_letter}")
                print(f"Lowest grade: {lowest} → {low_letter}")
            else:
                print("No grades available.")

        elif choice == '7':
            print(f"Total students: {len(students)}")

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

main()