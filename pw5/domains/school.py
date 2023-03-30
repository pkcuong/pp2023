from .student import Student
from .course import Course
import math 
import numpy as np 
class School:
    def __init__(self):
        self.students = []
        self.courses = []
    def read_data(self,school):
        
        with open('students.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0].strip()
                id = data[1].strip()
                dob = data[2].strip()
                student = Student(name, id, dob)
                school.students.append(student)
        with open('courses.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                id = data[0].strip()
                name = data[1].strip()
                course = Course(id, name)
                school.courses.append(course)
        with open('marks.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                student_id = data[0].strip()
                course_id = data[1].strip()
                mark = float(data[2].strip())
                school.marks.append((student_id, course_id, mark))
        return school.students, school.courses, school.marks

    