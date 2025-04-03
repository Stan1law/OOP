import datetime

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}")

student_count = 300001

def generate_student_id():
    global student_count  
    year = datetime.datetime.now().year  
    student_count += 1  
    return f"{year}-{student_count}"  

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = generate_student_id()
        print(f"Generated Student ID: {student_id}")
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        course = input("Enter Student Course: ")
        self.students.append(Student(student_id, name, age, course))
        print("Student added successfully!\n")

    def display_students(self):
        if not self.students:
            print("No students found.\n")
            return
        print("\nStudent List:")
        for student in self.students:
            student.display_info()
        print()

    def remove_student(self):
        student_id = input("Enter Student ID to remove: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student removed successfully!\n")
                return
        print("Student not found.\n")

    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        for student in self.students:
            if student.student_id == student_id:
                print("Student Found:")
                student.display_info()
                return
        print("Student not found.\n")


def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Remove Student")
        print("4. Search Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sms.add_student()
        elif choice == '2':
            sms.display_students()
        elif choice == '3':
            sms.remove_student()
        elif choice == '4':
            sms.search_student()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
