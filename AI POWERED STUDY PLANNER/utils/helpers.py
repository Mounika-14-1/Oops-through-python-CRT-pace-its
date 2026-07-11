# ==========================================
# utils/helpers.py
# AI-Powered Study Planner
# Common Helper Functions
# ==========================================

from flask import session, redirect, url_for
from datetime import datetime


# ==========================================
# Check User Login
# ==========================================

def login_required():

    if "user_id" not in session:

        return False

    return True



# ==========================================
# Redirect If Not Logged In
# ==========================================

def require_login():

    if "user_id" not in session:

        return redirect(
            url_for("auth.login")
        )

    return None



# ==========================================
# Calculate Completion Percentage
# ==========================================

def calculate_percentage(
        completed_hours,
        target_hours
):

    if target_hours == 0:

        return 0


    percentage = (

        completed_hours

        /

        target_hours

    ) * 100


    if percentage > 100:

        percentage = 100


    return round(
        percentage,
        2
    )



# ==========================================
# Calculate Remaining Hours
# ==========================================

def remaining_hours(
        completed_hours,
        target_hours
):

    remaining = (

        target_hours

        -

        completed_hours

    )


    if remaining < 0:

        remaining = 0


    return remaining



# ==========================================
# Format Date
# ==========================================

def format_date(date):

    if not date:

        return ""


    if isinstance(
        date,
        str
    ):

        date = datetime.strptime(
            date,
            "%Y-%m-%d"
        )


    return date.strftime(
        "%d %B %Y"
    )



# ==========================================
# Format Time
# ==========================================

def format_time(time):

    if not time:

        return ""


    if isinstance(
        time,
        str
    ):

        time = datetime.strptime(
            time,
            "%H:%M"
        )


    return time.strftime(
        "%I:%M %p"
    )



# ==========================================
# Generate Study Session Time
# ==========================================

def calculate_session_time(
        total_hours,
        sessions
):

    if sessions == 0:

        return 0


    return round(

        total_hours / sessions,

        2

    )



# ==========================================
# Validate Email
# ==========================================

def validate_email(email):

    if "@" in email and "." in email:

        return True


    return False



# ==========================================
# Validate Password
# ==========================================

def validate_password(password):

    if len(password) < 6:

        return False


    return True



# ==========================================
# Clean Text Input
# ==========================================

def clean_text(text):

    if text:

        return text.strip()


    return ""



# ==========================================
# Generate Greeting Message
# ==========================================

def greeting_message(username):

    hour = datetime.now().hour


    if hour < 12:

        greeting = "Good Morning"


    elif hour < 17:

        greeting = "Good Afternoon"


    else:

        greeting = "Good Evening"


    return f"{greeting}, {username}!"



# ==========================================
# Study Priority Level
# ==========================================

def priority_level(
        percentage
):

    if percentage >= 80:

        return "Excellent"


    elif percentage >= 50:

        return "Good"


    elif percentage >= 30:

        return "Needs Improvement"


    else:

        return "Critical"



# ==========================================
# Generate AI Prompt
# ==========================================

def create_ai_prompt(
        subjects,
        hours,
        plan_type,
        exam_date
):

    prompt = f"""

Create a {plan_type} study plan.

Subjects:
{subjects}

Available Study Hours:
{hours}

Exam Date:
{exam_date}

Include:

- Study sessions
- Break timings
- Revision
- Practice tests
- Improvement tips

"""

    return prompt