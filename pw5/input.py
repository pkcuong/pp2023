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
        
        with open('students.txt', 'a') as file:
            file.write(f"{name}, {id}, {dob}\n")
    def input_course_info(self,school):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        school.courses.append(course)
        print("Course information saved successfully!")
        
        with open('courses.txt', 'a') as file:
            file.write(f"{id}, {name}\n")
    def input_student_marks(self,school):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = input("Enter mark: ")
        mark = math.floor(float(mark) * 10) / 10 # round down to 1-digit decimal
        student = next((s for s in school.students if s.id == student_id), None)
        if student:
            student.marks[course_id] = mark
            print("Mark saved successfully!")
            with open('marks.txt', 'a') as file:
                file.write(f"{student_id}, {course_id}, {mark}\n")
        else:
            print("No student found for the given ID.")
        pass
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


