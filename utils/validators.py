
def validate_student_id(student_id):
    if not student_id or not student_id.strip():
        return False
    return True


def validate_name(name):
    if not name or not name.strip():
        return False
    return True


def validate_age(age):
    if not age or not str(age).strip():
        return False

    clean_age = str(age).strip()
    if not clean_age.isdigit():
        return False
    
    age_num = int(clean_age)
    if age_num < 1 or age_num > 100:
        return False
    return True


def validate_email(email):
    if not email or not str(email).strip():
        return False

    clean_email= str(email).strip()

    if clean_email.count("@") != 1 or "." not in clean_email:
        return False
    
    parts = clean_email.split("@")
    username = parts[0]
    domain = parts[1]

    if not username or "." not in domain:
        return False

    domain_parts = domain.split(".")
    if not domain_parts[0] or len(domain_parts[-1]) < 2:
        return False

    return True


def validate_department(department):
    if not department or not department.strip():
        return False

    return True