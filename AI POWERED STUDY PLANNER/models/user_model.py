# ==========================================
# models/user_model.py
# AI-Powered Study Planner
# ==========================================

from werkzeug.security import generate_password_hash, check_password_hash
from database.db import fetch_one, fetch_all, execute_insert, execute_query


class User:

    # -----------------------------
    # Register New User
    # -----------------------------
    @staticmethod
    def register(username, email, password, college, course, study_year, daily_goal):

        # Check if email already exists
        existing_user = fetch_one(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        if existing_user:
            return False

        hashed_password = generate_password_hash(password)

        query = """
            INSERT INTO users
            (username, email, password, college, course, study_year, daily_goal)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        execute_insert(
            query,
            (
                username,
                email,
                hashed_password,
                college,
                course,
                study_year,
                daily_goal
            )
        )

        return True

    # -----------------------------
    # Login
    # -----------------------------
    @staticmethod
    def login(email, password):

        user = fetch_one(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        if user and check_password_hash(user["password"], password):
            return user

        return None

    # -----------------------------
    # Get User By ID
    # -----------------------------
    @staticmethod
    def get_user(user_id):

        return fetch_one(
            "SELECT * FROM users WHERE id=%s",
            (user_id,)
        )

    # -----------------------------
    # Get User By Email
    # -----------------------------
    @staticmethod
    def get_by_email(email):

        return fetch_one(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

    # -----------------------------
    # Get All Users
    # -----------------------------
    @staticmethod
    def get_all():

        return fetch_all(
            "SELECT * FROM users ORDER BY id DESC"
        )

    # -----------------------------
    # Update Profile
    # -----------------------------
    @staticmethod
    def update_profile(
        user_id,
        username,
        college,
        course,
        study_year,
        daily_goal,
        about
    ):

        query = """
        UPDATE users
        SET
            username=%s,
            college=%s,
            course=%s,
            study_year=%s,
            daily_goal=%s,
            about=%s
        WHERE id=%s
        """

        execute_query(
            query,
            (
                username,
                college,
                course,
                study_year,
                daily_goal,
                about,
                user_id
            )
        )

    # -----------------------------
    # Change Password
    # -----------------------------
    @staticmethod
    def change_password(user_id, new_password):

        hashed_password = generate_password_hash(new_password)

        execute_query(
            """
            UPDATE users
            SET password=%s
            WHERE id=%s
            """,
            (
                hashed_password,
                user_id
            )
        )

    # -----------------------------
    # Delete User
    # -----------------------------
    @staticmethod
    def delete(user_id):

        execute_query(
            "DELETE FROM users WHERE id=%s",
            (user_id,)
        )

    # -----------------------------
    # Dashboard Statistics
    # -----------------------------
    @staticmethod
    def dashboard_statistics(user_id):

        total_subjects = fetch_one(
            """
            SELECT COUNT(*) AS total
            FROM subjects
            WHERE user_id=%s
            """,
            (user_id,)
        )

        total_plans = fetch_one(
            """
            SELECT COUNT(*) AS total
            FROM study_plans
            WHERE user_id=%s
            """,
            (user_id,)
        )

        completed_plans = fetch_one(
            """
            SELECT COUNT(*) AS total
            FROM study_plans
            WHERE user_id=%s
            AND status='Completed'
            """,
            (user_id,)
        )

        total_hours = fetch_one(
            """
            SELECT IFNULL(SUM(study_hours),0) AS hours
            FROM study_plans
            WHERE user_id=%s
            """,
            (user_id,)
        )

        return {
            "subjects": total_subjects["total"],
            "plans": total_plans["total"],
            "completed": completed_plans["total"],
            "hours": total_hours["hours"]
        }