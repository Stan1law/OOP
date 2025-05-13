class Student:
    def __init__(self, name="", age=0, program="", year=0, course=""):
        self.name = name
        self.age = age
        self.program = program
        self.year = year
        self.course = course

    def display_student_info(self):
        print(f"name: {self.name}, age: {self.age}, program: {self.program}, year: {self.year}, course: {self.course}")


def main():
    stud = Student(name="Stanley", age=20, program="BSCS", year=1, course="OOP")
    stud.display_student_info()


if __name__ == "__main__":
    main()

