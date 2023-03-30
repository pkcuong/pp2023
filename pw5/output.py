
from domains.school import School
from domains.student import Student
from domains.course import Course
import math 

class Output:
    def list_courses(self,school):
        print("List of courses:")
        for course in school.courses:
            print(course.id, course.name)

    def list_students(self,school):
        print("List of students:")
        for student in school.students:
            print(student.id, student.name)

    def list_marks(self,school):
        print("List of marks:")
        for student in school.students:
            print("Student ID:", student.id)
            for course_id, mark in student.marks.items():
                print("Course ID:", course_id, "Mark:", mark)
    def list_students_by_gpa(self,school):
        students_by_gpa = sorted(school.students, key=school.calculate_gpa, reverse=True)
        print("List of students by GPA descending:")
        for student in students_by_gpa:
            print("Student ID:", student.id, "Name:", student.name, "GPA:", school.calculate_gpa(student))

    def show_student_marks(self,school):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = next((s for s in school.students if s.id == student_id), None)
        if student and course_id in student.marks:
            mark = student.marks[course_id]
            print("Student ID:", student_id, "Course ID:", course_id, "Mark:", mark)
        else:
            print("No mark found for the given student ID and course ID.")
    
    
