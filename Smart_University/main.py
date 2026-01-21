from models.student import Student
from models.faculty import Faculty
from models.course import Course
from utils.file_manager import FileManager

from decorators.logger import log_execution
from decorators.timer import performance_timer

students = []
courses = []
faculties = []


@log_execution
@performance_timer
def menu():
    while True:
        print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Enroll\n5 Performance\n6 Compare\n7 Report\n8 Exit")
        choice = input("Choice: ")

        if choice == "1":
            sid = input("ID: ")
            name = input("Name: ")
            department = input("Department: ")
            semester = int(input("Semester: "))
            marks = list(map(int, input("Marks (5 subjects): ").split()))
            students.append(Student(sid, name, department, semester, marks))

            print("Student Created Successfully")
            print("--------------------------------")
            print(f"ID        : {sid}")
            print(f"Name      : {name}")
            print(f"Department: {department}")
            print(f"Semester  : {semester}")


        elif choice == "2":
            fid = input("ID: ")
            name = input("Name: ")
            sal = float(input("Salary: "))
            faculty = Faculty(fid, name, sal)
            faculties.append(faculty)

            print("Faculty created successfully")
            print(faculty.get_details())


        elif choice == "3":
            cid = input("Course ID: ")
            title = input("Title: ")
            credits = int(input("Credits: "))
            courses.append(Course(cid, title, credits))
            print("Course created")

        elif choice == "4":
            students[0].enroll(courses[0])
            print("Enrollment successful")

        elif choice == "5":
            s = students[0]
            print(s.get_details(), "Grade:", s.calculate_performance())

        elif choice == "6":
            print(students[0] > students[-1])

        elif choice == "7":
            FileManager.save_students_json(students, "data/students.json")
            FileManager.save_students_csv(students, "data/students_report.csv")

            if faculties:
                FileManager.save_faculty_to_json(faculties, "data/faculty.json")
                FileManager.save_faculty_csv(faculties, "data/faculty_report.csv")

            if courses:
                FileManager.save_courses_json(courses, "data/courses.json")
                FileManager.save_courses_csv(courses, "data/courses.csv")

            print("All reports generated successfully")


        elif choice == "8":
            print("Exiting system")
            break

        elif choice == "9":
            if not courses:
                print("No courses available")
            else:
                print("\nAvailable Courses:")
                for course in courses:
                    print(f"{course.course_id} | {course.course_name} | {course.credit_points}")


if __name__ == "__main__":
    menu()
