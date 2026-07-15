from datetime import date
import calendar


def calculate_age(birth_date):
    """
    Calculate age in years, months, and days.

    Args:
        birth_date (date): User's date of birth.

    Returns:
        tuple: (years, months, days)
    """
    today = date.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust days if negative
    if days < 0:
        previous_month = today.month - 1 or 12
        previous_year = today.year if today.month != 1 else today.year - 1

        days += calendar.monthrange(previous_year, previous_month)[1]
        months -= 1

    # Adjust months if negative
    if months < 0:
        months += 12
        years -= 1

    return years, months, days