from models.person import Person
from descriptors.marks import MarksDescriptor


class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, pid, name,  department,semester, marks):
        super().__init__(pid, name)
        self.department = department
        self.semester = semester
        self.marks = marks
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def calculate_performance(self):
        avg = sum(m for m in self.marks) / len(self.marks)  # generator used
        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        else:
            grade = "C"
        return avg, grade

    def get_details(self):  # POLYMORPHISM
        return (
            f"Name      : {self.name}\n"
            f"Role      : Student\n"
            f"Department: {self.department}"
        )

    def __gt__(self, other):  # OPERATOR OVERLOADING
        return sum(self.marks) / len(self.marks) > sum(other.marks) / len(other.marks)

    def __add__(self, other):
        return sum(c.credits for c in self.courses + other.courses)
