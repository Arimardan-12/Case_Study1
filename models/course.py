

class Course:
    def __init__(self, course_id, course_name, credit_points, faculty=None):
        self.course_id = course_id
        self.course_name = course_name
        self.credit_points = credit_points
        self.faculty = faculty


def __str__(self):
        return f"{self.course_id} | {self.course_name} | {self.credit_points} credits |{self.faculty}"
