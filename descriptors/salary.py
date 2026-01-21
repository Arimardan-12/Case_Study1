
class SalaryDescriptor:
    def __get__(self, instance, owner):
        return "CONFIDENTIAL"

    def __set__(self, instance, value):
        instance.__dict__["_salary"] = value