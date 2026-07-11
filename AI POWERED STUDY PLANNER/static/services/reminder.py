# ==========================================
# utils/reminder.py
# AI-Powered Study Planner
# Study Reminder System
# ==========================================

from datetime import datetime, timedelta

from database.db import fetch_all, fetch_one, execute_insert, execute_query


class Reminder:


    # ==========================================
    # Create Reminder
    # ==========================================

    @staticmethod
    def create_reminder(
        user_id,
        title,
        message,
        reminder_date,
        reminder_time
    ):

        query = """

        INSERT INTO reminders

        (
            user_id,
            title,
            message,
            reminder_date,
            reminder_time
        )

        VALUES

        (
            %s,
            %s,
            %s,
            %s,
            %s
        )

        """

        return execute_insert(
            query,
            (
                user_id,
                title,
                message,
                reminder_date,
                reminder_time
            )
        )



    # ==========================================
    # Get User Reminders
    # ==========================================

    @staticmethod
    def get_reminders(user_id):

        query = """

        SELECT *

        FROM reminders

        WHERE user_id=%s

        ORDER BY reminder_date, reminder_time

        """

        return fetch_all(
            query,
            (user_id,)
        )



    # ==========================================
    # Get Today's Reminders
    # ==========================================

    @staticmethod
    def today_reminders(user_id):

        today = datetime.now().date()


        query = """

        SELECT *

        FROM reminders

        WHERE

        user_id=%s

        AND reminder_date=%s

        ORDER BY reminder_time

        """

        return fetch_all(
            query,
            (
                user_id,
                today
            )
        )



    # ==========================================
    # Mark Reminder Completed
    # ==========================================

    @staticmethod
    def complete_reminder(reminder_id):

        query = """

        UPDATE reminders

        SET status='Completed'

        WHERE id=%s

        """

        execute_query(
            query,
            (reminder_id,)
        )



    # ==========================================
    # Delete Reminder
    # ==========================================

    @staticmethod
    def delete_reminder(reminder_id):

        query = """

        DELETE FROM reminders

        WHERE id=%s

        """

        execute_query(
            query,
            (reminder_id,)
        )



    # ==========================================
    # Generate Automatic Study Reminder
    # ==========================================

    @staticmethod
    def generate_study_reminder(
        user_id,
        subject,
        study_time,
        study_date
    ):


        title = "Study Reminder"


        message = (

            f"Your {subject} study session "
            f"is scheduled at {study_time}. "
            "Stay focused and complete your goal!"

        )


        return Reminder.create_reminder(

            user_id,

            title,

            message,

            study_date,

            study_time

        )



    # ==========================================
    # Upcoming Reminders
    # ==========================================

    @staticmethod
    def upcoming_reminders(user_id):

        today = datetime.now().date()


        query = """

        SELECT *

        FROM reminders

        WHERE

        user_id=%s

        AND reminder_date >= %s

        AND status='Pending'

        ORDER BY reminder_date, reminder_time

        """

        return fetch_all(

            query,

            (
                user_id,
                today
            )

        )



    # ==========================================
    # Reminder Count
    # ==========================================

    @staticmethod
    def reminder_count(user_id):

        result = fetch_one(

            """

            SELECT COUNT(*) AS total

            FROM reminders

            WHERE user_id=%s

            AND status='Pending'

            """,

            (user_id,)

        )


        return result["total"]