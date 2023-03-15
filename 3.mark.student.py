import math
import numpy as np


class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student_info(self):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        dob = input("Enter student date of birth: ")
        student = Student(name, id, dob)
        self.students.append(student)
        print("Student information saved successfully!")

    def input_course_info(self):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        self.courses.append(course)
        print("Course information saved successfully!")

    def input_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = input("Enter mark: ")
        mark = math.floor(float(mark) * 10) / 10 # round down to 1-digit decimal
        student = next((s for s in self.students if s.id == student_id), None)
        if student:
            student.marks[course_id] = mark
            print("Mark saved successfully!")
        else:
            print("No student found for the given ID.")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course.id, course.name)

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student.id, student.name)

    def list_marks(self):
        print("List of marks:")
        for student in self.students:
            print("Student ID:", student.id)
            for course_id, mark in student.marks.items():
                print("Course ID:", course_id, "Mark:", mark)

    def calculate_gpa(self, student):
        credits = []
        marks = []
        for course_id, mark in student.marks.items():
            course = next((c for c in self.courses if c.id == course_id), None)
            if course:
                credits.append(3) # assuming all courses have 3 credits
                marks.append(float(mark))
        if credits and marks:
            gpa = np.average(marks, weights=credits)
            return round(gpa, 2)
        else:
            return 0.0

    def list_students_by_gpa(self):
        students_by_gpa = sorted(self.students, key=self.calculate_gpa, reverse=True)
        print("List of students by GPA descending:")
        for student in students_by_gpa:
            print("Student ID:", student.id, "Name:", student.name, "GPA:", self.calculate_gpa(student))

    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = next((s for s in self.students if s.id == student_id), None)
        if student and course_id in student.marks:
            mark = student.marks[course_id]
            print("Student ID:", student_id, "Course ID:", course_id, "Mark:", mark)
        else:
            print("No mark found for the given student ID and course ID.")

    def run(self):
       

        while True:
            print("Choose an option: ")
            print("1. Input student information" )
            print("2. Input course information")
            print("3. Input student marks")
            print("4. List courses")
            print("5. List students")
            print("6. List marks")
            print("7. Show student marks for a given course")
            print("8. List students by GPA descending")
            print("0. Exit")
            choice = input("enter your choice : ")
            if choice == "1":
                self.input_student_info()
            elif choice == "2":
                self.input_course_info()
            elif choice == "3":
                self.input_student_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.list_marks()
            elif choice == "7":
                self.show_student_marks()
            elif choice == "8":
                self.list_students_by_gpa()
            elif choice == "0":
                 break
            else:
                print("Invalid choice. Please try again.\\n")
                
                
school = School()
school.run()
