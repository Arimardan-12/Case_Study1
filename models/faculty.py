from models.person import Person
from descriptors.salary import SalaryDescriptor


class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, pid, name, salary):
        super().__init__(pid, name)
        self.salary = salary

    def calculate_performance(self):
        return "Excellent"

    def get_details(self):
        return f"Faculty {self.name}"