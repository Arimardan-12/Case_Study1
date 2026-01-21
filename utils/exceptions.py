class UniversityError(Exception):
    pass


class InvalidMarksError(UniversityError):
    pass


class DuplicateStudentError(UniversityError):
    pass


class UnauthorizedAccessError(UniversityError):
    pass


class FileMissingError(UniversityError):
    pass
