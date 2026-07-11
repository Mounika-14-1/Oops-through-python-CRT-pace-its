# ==========================================
# utils/constants.py
# AI-Powered Study Planner
# Application Constants
# ==========================================


# ==========================================
# Application Information
# ==========================================

APP_NAME = "AI-Powered Study Planner"

APP_VERSION = "1.0.0"



# ==========================================
# User Roles
# ==========================================

ROLE_STUDENT = "Student"

ROLE_ADMIN = "Admin"



# ==========================================
# Study Plan Types
# ==========================================

DAILY_PLAN = "Daily"

WEEKLY_PLAN = "Weekly"

MONTHLY_PLAN = "Monthly"


PLAN_TYPES = [

    DAILY_PLAN,

    WEEKLY_PLAN,

    MONTHLY_PLAN

]



# ==========================================
# Study Plan Status
# ==========================================

STATUS_PENDING = "Pending"

STATUS_COMPLETED = "Completed"


PLAN_STATUS = [

    STATUS_PENDING,

    STATUS_COMPLETED

]



# ==========================================
# Subject Difficulty Levels
# ==========================================

DIFFICULTY_EASY = "Easy"

DIFFICULTY_MEDIUM = "Medium"

DIFFICULTY_HARD = "Hard"


DIFFICULTY_LEVELS = [

    DIFFICULTY_EASY,

    DIFFICULTY_MEDIUM,

    DIFFICULTY_HARD

]



# ==========================================
# Subject Priority Levels
# ==========================================

PRIORITY_LOW = "Low"

PRIORITY_MEDIUM = "Medium"

PRIORITY_HIGH = "High"


PRIORITY_LEVELS = [

    PRIORITY_LOW,

    PRIORITY_MEDIUM,

    PRIORITY_HIGH

]



# ==========================================
# Progress Constants
# ==========================================

EXCELLENT_PROGRESS = 80

GOOD_PROGRESS = 50

LOW_PROGRESS = 30



# ==========================================
# Default Study Settings
# ==========================================

DEFAULT_DAILY_HOURS = 4

DEFAULT_BREAK_TIME = 15

DEFAULT_SESSION_COUNT = 3



# ==========================================
# Password Settings
# ==========================================

MIN_PASSWORD_LENGTH = 8



# ==========================================
# Pagination
# ==========================================

ITEMS_PER_PAGE = 10



# ==========================================
# AI Configuration
# ==========================================

AI_MODEL_NAME = "gemini-1.5-flash"

AI_MAX_TOKENS = 2048



# ==========================================
# Date & Time Formats
# ==========================================

DATE_FORMAT = "%Y-%m-%d"

TIME_FORMAT = "%H:%M"

DISPLAY_DATE_FORMAT = "%d %B %Y"

DISPLAY_TIME_FORMAT = "%I:%M %p"



# ==========================================
# Reminder Settings
# ==========================================

REMINDER_PENDING = "Pending"

REMINDER_COMPLETED = "Completed"


REMINDER_TYPES = [

    "Study",

    "Exam",

    "Revision"

]



# ==========================================
# Flash Messages
# ==========================================

LOGIN_SUCCESS = "Login successful!"

LOGIN_FAILED = "Invalid email or password."

REGISTER_SUCCESS = "Registration successful!"

LOGOUT_SUCCESS = "Logged out successfully!"

PROFILE_UPDATED = "Profile updated successfully!"

PLAN_CREATED = "Study plan created successfully!"

PLAN_DELETED = "Study plan deleted successfully!"

PROGRESS_UPDATED = "Progress updated successfully!"



# ==========================================
# Error Messages
# ==========================================

ERROR_REQUIRED_FIELD = "This field is required."

ERROR_INVALID_EMAIL = "Invalid email address."

ERROR_PASSWORD = "Invalid password."

ERROR_NOT_FOUND = "Data not found."

ERROR_UNAUTHORIZED = "Please login first."



# ==========================================
# AI Prompt Templates
# ==========================================

AI_STUDY_PROMPT = """

Create a personalized study plan.

Subjects:
{subjects}

Study Hours:
{hours}

Plan Type:
{plan_type}

Exam Date:
{exam_date}

Include:

- Study sessions
- Breaks
- Revision
- Practice tests
- Improvement suggestions

"""



# ==========================================
# Days of Week
# ==========================================

WEEK_DAYS = [

    "Monday",

    "Tuesday",

    "Wednesday",

    "Thursday",

    "Friday",

    "Saturday",

    "Sunday"

]