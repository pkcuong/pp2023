students = []
courses = []
marks = {}

def input_student_info():
    name = input("Enter student name: ")
    id = input("Enter student ID: ")
    dob = input("Enter student date of birth: ")
    student = {"name": name, "id": id, "dob": dob}
    students.append(student)
    print("Student information saved successfully!")


def input_course_info():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    course = {"id": id, "name": name}
    courses.append(course)
    print("Course information saved successfully!")


def input_student_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    mark = input("Enter mark: ")
    student_marks = marks.get(student_id, {})
    student_marks[course_id] = mark
    marks[student_id] = student_marks
    print("Mark saved successfully!")


def list_courses():
    print("List of courses:")
    for course in courses:
        print(course["id"], course["name"])


def list_students():
    print("List of students:")
    for student in students:
        print(student["id"], student["name"])


def list_marks():
    print("List of marks:")
    for student_id, student_marks in marks.items():
        print("Student ID:", student_id)
        for course_id, mark in student_marks.items():
            print("Course ID:", course_id, "Mark:", mark)


def show_student_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    student_marks = marks.get(student_id, {})
    mark = student_marks.get(course_id)
    if mark:
        print("Student ID:", student_id, "Course ID:", course_id, "Mark:", mark)
    else:
        print("No mark found for the given student ID and course ID.")


while True:
    print("Choose an option:")
    print("1. Input student information")
    print("2. Input course information")
    print("3. Input student marks")
    print("4. List courses")
    print("5. List students")
    print("6. List marks")
    print("7. Show student marks for a given course")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_student_info()
    elif choice == "2":
        input_course_info()
    elif choice == "3":
        input_student_marks()
    elif choice == "4":
        list_courses()
    elif choice == "5":
        list_students()
    elif choice == "6":
        list_marks()
    elif choice == "7":
        show_student_marks()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")