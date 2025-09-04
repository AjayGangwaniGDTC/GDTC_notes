import re

def validate_student_data(data):
    if not data["id"].isdigit():
        return False, "ID must be an integer."
    if not data["name"].isalpha():
        return False, "Name must contain only letters."
    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', data["email"]):
        return False, "Invalid email format."
    if not data["phone"].isdigit():
        return False, "Phone must be numeric."
    return True, "Valid"