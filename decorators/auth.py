from utils.exceptions import UnauthorizedAccessError


def admin_only(func):
    def wrapper(*args, **kwargs):
        role = kwargs.get("role", "user")
        if role != "admin":
            raise UnauthorizedAccessError("Admin privileges required.")
        return func(*args, **kwargs)
    return wrapper
