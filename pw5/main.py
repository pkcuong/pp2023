from domains.school import School
from input import Input as InputSchool
from output import Output as OutputSchool



def main():
    school = School()
    input_school = InputSchool()
    output_school = OutputSchool()
    

    while True:
        print("Choose an option:")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input student marks")
        print("4. List courses")
        print("5. List students")
        print("6. List marks")
        print("7. Show student marks for a given course")
        print("8. List students by GPA descending")
        
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            input_school.input_student_info(school)
            
        elif choice == "2":
            input_school.input_course_info(school)
            
        elif choice == "3":
            input_school.input_student_marks(school)
            
        elif choice == "4":
            output_school.list_courses(school)
        elif choice == "5":
            output_school.list_students(school)
        elif choice == "6":
            output_school.list_marks(school)
        elif choice == "7":
            output_school.show_student_marks(school)
        elif choice == "8":
            output_school.list_students_by_gpa(school)
        
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

