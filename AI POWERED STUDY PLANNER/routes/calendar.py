from flask import Blueprint, render_template, request
import calendar as py_calendar
from datetime import datetime

calendar = Blueprint("calendar", __name__)

@calendar.route("/calendar")
def calendar_page():

    today = datetime.today()

    month = request.args.get("month", default=today.month, type=int)
    year = request.args.get("year", default=today.year, type=int)

    # Fix month/year boundaries
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    calendar_data = py_calendar.monthcalendar(year, month)

    # Previous month values
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year

    # Next month values
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    return render_template(
        "calendar.html",
        calendar_data=calendar_data,
        month=py_calendar.month_name[month],
        year=year,
        prev_month=prev_month,
        prev_year=prev_year,
        next_month=next_month,
        next_year=next_year
    )