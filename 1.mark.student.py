
students = {}
courses = {}
marks = {}
def input_students():
    num_s = int(input("Enter the number of : "))
    for i in range(num_s):
        student_id = input("Enter the student ID: ")
        student_name = input("Enter the student name: ")
        student_dob = input("Enter the student date of birth: ")
        students[student_id] = {"name": student_name, "dob": student_dob}
def input_courses():
    num_c = int(input("Enter the number of courses: "))
    for i in range(num_c):
        course_id = input("Enter the course ID: ")
        course_name = input("Enter the course name: ")
        courses[course_id] = {"name": course_name}
def input_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        mark = int(input(f"Enter the mark for {students[student_id]['name']}: "))
        if student_id not in marks:
            marks[student_id] = {}
        marks[student_id][course_id] = mark
def list_courses():
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]['name']}")
def list_students():
    for student_id in students:
        print(f"{student_id}: {students[student_id]['name']}")
def show_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        if student_id in marks and course_id in marks[student_id]:
            print(f"{students[student_id]['name']}: {marks[student_id][course_id]}")
        else:
            print(f"{students[student_id]['name']}: N/A")
input_students()
input_courses()
while True :
    print("Options: ")
    print("1.list students")
    print("2.list course")
    print("3.input marks")
    print("4.show marks ")
    print("5.quit")
    choice = input("enter choices")
    if choice == "1":
        list_students()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        input_marks()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        break
    else:
        print("invalid option!")

