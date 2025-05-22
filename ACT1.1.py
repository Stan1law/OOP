# Create a program that defines a Student class using full object-oriented programming principles. The class should encapsulate relevant student details and include functionality to display them. Instantiate and utilize the class in a separate section of the program to simulate object usage.
# Name: Stanley
# Age: 20
# Program: BSCS
# Year Level: 1
# Course: OOP

class Student:
    def __init__(self, name, age, program, year_level, course):
        self.__name = name
        self.__age = int(age)
        self.__program = program
        self.__year_level =     year_level
        self.__course = course
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
        
    def get_program(self):
        return self.__program
        
    def get_year_level(self):
        return self.__year_level
    
    def get_course(self):
        return self.__course
        
    def display_stud_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Program: {self.__program}")
        print(f"Year Level: {self.__year_level}")
        print(f"Course: {self.__course}")
        
if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    program = input("Enter your program: ")
    year_level = input("Enter your year level: ")
    course = input("Enter your course: ")
    
    stud = Student(name, age, program, year_level, course)
    
    stud.display_stud_info()
    
