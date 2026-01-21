import json
import csv
import os


class FileManager:

    # ============================
    # COMMON UTIL
    # ============================
    @staticmethod
    def ensure_data_directory(file_path):
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            print(f"[INFO] Created directory: {directory}")

    # ============================
    # STUDENT FILE HANDLING
    # ============================
    @staticmethod
    def save_students_json(students, file_path):
        FileManager.ensure_data_directory(file_path)

        data = []
        for student in students:
            avg, grade = student.calculate_performance()
            data.append({
                "id": student.pid,
                "name": student.name,
                "department": student.department,
                "semester": student.semester,
                "marks": student.marks,
                "average": round(avg, 2),
                "grade": grade
            })

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        print("[FILE] students.json saved successfully")

    @staticmethod
    def save_students_csv(students, file_path):
        FileManager.ensure_data_directory(file_path)

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

            for s in students:
                avg, grade = s.calculate_performance()
                writer.writerow([
                    s.pid,
                    s.name,
                    s.department,
                    round(avg, 2),
                    grade
                ])

        print("[FILE] students_report.csv generated successfully")

    # ============================
    # FACULTY FILE HANDLING
    # ============================
    @staticmethod
    def save_faculty_to_json(faculties, file_path):
        FileManager.ensure_data_directory(file_path)

        with open(file_path, "w") as file:
            json.dump({
                faculty.pid: {
                    "name": faculty.name,
                    "salary": faculty.salary
                }
                for faculty in faculties
            }, file, indent=4)

        print("[FILE] faculty.json saved successfully")

    @staticmethod
    def save_faculty_csv(faculties, file_path):
        FileManager.ensure_data_directory(file_path)

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Faculty ID", "Name", "Salary"])

            for faculty in faculties:
                writer.writerow([
                    faculty.pid,
                    faculty.name,
                    faculty.salary
                ])

        print("[FILE] faculty_report.csv saved successfully")

    # ============================
    # COURSE FILE HANDLING
    # ============================
    @staticmethod
    def save_courses_json(courses, file_path):
        FileManager.ensure_data_directory(file_path)

        with open(file_path, "w") as file:
            json.dump({
                course.course_id: {
                    "title": course.course_name,
                    "credits": course.credit_points,
                    "faculty": course.faculty.name if course.faculty else None
                }
                for course in courses
            }, file, indent=4)

        print("[FILE] courses.json saved successfully")

    @staticmethod
    def save_courses_csv(courses, file_path):
        FileManager.ensure_data_directory(file_path)

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Course ID", "Title", "Credits", "Faculty"])

            for course in courses:
                writer.writerow([
                    course.course_id,
                    course.course_name,
                    course.credit_points,
                    course.faculty.name if course.faculty else "Not Assigned"
                ])

        print("[FILE] courses.csv saved successfully")
