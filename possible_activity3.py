class StudentGrade:
    def __init__(self, student_name, subject, grade=0.0):
        self.__student_name = student_name  # Private attribute
        self.__subject = subject  # Private attribute
        self.__grade = grade  # Private attribute

    # Setter for grade with validation
    def set_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.__grade = grade

    # Getter for grade
    def get_grade(self):
        return self.__grade

    # Method to check if the student is passing
    def is_passing(self):
        return self.__grade >= 75

    # Method to display student information
    def display_student_info(self):
        status = "Passing" if self.is_passing() else "Failing"
        print(f"Student Name: {self.__student_name}")
        print(f"Subject: {self.__subject}")
        print(f"Grade: {self.__grade}")
        print(f"Status: {status}")


# Example usage with user interaction
if __name__ == "__main__":
    students = []

    while True:
        print("\nGrade Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                student_name = input("Enter student name: ")
                subject = input("Enter subject: ")
                try:
                    grade = float(input("Enter grade (0-100): "))
                    student = StudentGrade(student_name, subject)
                    student.set_grade(grade)
                    students.append(student)
                    print(f"Student {student_name} added successfully.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == 2:
                if not students:
                    print("No students available.")
                else:
                    print("\nStudent List:")
                    for student in students:
                        student.display_student_info()
                        print("-" * 30)
            elif choice == 3:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")



# Grade Management System
# Problem: Create a StudentGrade class with private attributes: studentName, subject, grade.
# Methods:

# setGrade(double grade) – only allow grades between 0 and 100

# getGrade()

# isPassing() – returns true if grade >= 75

# Twist: Accept multiple students via loop and determine who passed/failed.