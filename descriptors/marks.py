from utils.exceptions import InvalidMarksError

class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("_marks", [])

    def __set__(self, instance, value):
        if not all(0 <= m <= 100 for m in value):
            raise InvalidMarksError("Marks should be between 0 and 100")
        instance.__dict__["_marks"] = value
