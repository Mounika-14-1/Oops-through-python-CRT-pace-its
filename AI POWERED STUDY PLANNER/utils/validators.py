# ==========================================
# utils/validators.py
# AI-Powered Study Planner
# Input Validation Functions
# ==========================================

import re
from datetime import datetime



# ==========================================
# Validate Email
# ==========================================

def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(
        re.match(
            pattern,
            email
        )
    )



# ==========================================
# Validate Username
# ==========================================

def validate_username(username):

    if not username:

        return False


    if len(username) < 3:

        return False


    if len(username) > 50:

        return False


    return True



# ==========================================
# Validate Password
# ==========================================

def validate_password(password):

    if not password:

        return False


    # Minimum 8 characters

    if len(password) < 8:

        return False


    # Must contain uppercase

    if not re.search(
        r"[A-Z]",
        password
    ):

        return False


    # Must contain lowercase

    if not re.search(
        r"[a-z]",
        password
    ):

        return False


    # Must contain number

    if not re.search(
        r"[0-9]",
        password
    ):

        return False


    return True



# ==========================================
# Validate Confirm Password
# ==========================================

def validate_confirm_password(
        password,
        confirm_password
):

    return password == confirm_password



# ==========================================
# Validate Subject Name
# ==========================================

def validate_subject(subject_name):

    if not subject_name:

        return False


    if len(subject_name) < 2:

        return False


    if len(subject_name) > 100:

        return False


    return True



# ==========================================
# Validate Study Hours
# ==========================================

def validate_study_hours(hours):

    try:

        hours = float(hours)


        if hours <= 0:

            return False


        if hours > 24:

            return False


        return True


    except:

        return False



# ==========================================
# Validate Plan Type
# ==========================================

def validate_plan_type(plan_type):

    allowed_types = [

        "Daily",
        "Weekly",
        "Monthly"

    ]


    return plan_type in allowed_types



# ==========================================
# Validate Date
# ==========================================

def validate_date(date):

    try:

        datetime.strptime(
            date,
            "%Y-%m-%d"
        )

        return True


    except:

        return False



# ==========================================
# Validate Exam Date
# ==========================================

def validate_exam_date(exam_date):

    if not validate_date(exam_date):

        return False


    exam = datetime.strptime(
        exam_date,
        "%Y-%m-%d"
    )


    today = datetime.now()


    if exam < today:

        return False


    return True



# ==========================================
# Validate Priority
# ==========================================

def validate_priority(priority):

    allowed = [

        "Low",
        "Medium",
        "High"

    ]


    return priority in allowed



# ==========================================
# Validate Difficulty
# ==========================================

def validate_difficulty(level):

    allowed = [

        "Easy",
        "Medium",
        "Hard"

    ]


    return level in allowed



# ==========================================
# Validate Profile Data
# ==========================================

def validate_profile(
        username,
        college,
        course
):

    if not username:

        return False


    if not college:

        return False


    if not course:

        return False


    return True



# ==========================================
# Validate Registration Form
# ==========================================

def validate_registration(
        username,
        email,
        password,
        confirm_password
):

    errors = []


    if not validate_username(username):

        errors.append(
            "Invalid username"
        )


    if not validate_email(email):

        errors.append(
            "Invalid email address"
        )


    if not validate_password(password):

        errors.append(
            "Password must contain 8 characters, uppercase, lowercase and number"
        )


    if not validate_confirm_password(
        password,
        confirm_password
    ):

        errors.append(
            "Passwords do not match"
        )


    return errors



# ==========================================
# Validate Study Plan Form
# ==========================================

def validate_study_plan(
        plan_type,
        hours,
        exam_date
):

    errors = []


    if not validate_plan_type(plan_type):

        errors.append(
            "Invalid plan type"
        )


    if not validate_study_hours(hours):

        errors.append(
            "Invalid study hours"
        )


    if exam_date and not validate_exam_date(exam_date):

        errors.append(
            "Invalid exam date"
        )


    return errors