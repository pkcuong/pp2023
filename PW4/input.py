from domains.school import School
import math
from domains.student import Student
from domains.course import Course


class Input:
    def input_student_info(self,school):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        dob = input("Enter student date of birth: ")
        student = Student(name, id, dob)
        school.students.append(student)
        print("Student information saved successfully!")
        pass

    def input_course_info(self,school):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        school.courses.append(course)
        print("Course information saved successfully!")
        pass

    def input_student_marks(self,school):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = input("Enter mark: ")
        mark = math.floor(float(mark) * 10) / 10 # round down to 1-digit decimal
        student = next((s for s in school.students if s.id == student_id), None)
        if student:
            student.marks[course_id] = mark
            print("Mark saved successfully!")
        else:
            print("No student found for the given ID.")
        pass
    