# ==========================================
# models/subject_model.py
# AI-Powered Study Planner
# ==========================================

from database.db import fetch_one, fetch_all, execute_insert, execute_query


class Subject:

    # ==========================================
    # Add Subject
    # ==========================================
    @staticmethod
    def add_subject(user_id, subject_name, difficulty, priority):

        query = """
        INSERT INTO subjects
        (
            user_id,
            subject_name,
            difficulty,
            priority
        )
        VALUES
        (
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
                subject_name,
                difficulty,
                priority
            )
        )

    # ==========================================
    # Get Subject By ID
    # ==========================================
    @staticmethod
    def get_subject(subject_id):

        query = """
        SELECT *
        FROM subjects
        WHERE id=%s
        """

        return fetch_one(
            query,
            (subject_id,)
        )

    # ==========================================
    # Get All Subjects of User
    # ==========================================
    @staticmethod
    def get_subjects(user_id):

        query = """
        SELECT *
        FROM subjects
        WHERE user_id=%s
        ORDER BY subject_name ASC
        """

        return fetch_all(
            query,
            (user_id,)
        )

    # ==========================================
    # Update Subject
    # ==========================================
    @staticmethod
    def update_subject(
        subject_id,
        subject_name,
        difficulty,
        priority
    ):

        query = """
        UPDATE subjects

        SET

            subject_name=%s,
            difficulty=%s,
            priority=%s

        WHERE id=%s
        """

        execute_query(
            query,
            (
                subject_name,
                difficulty,
                priority,
                subject_id
            )
        )

    # ==========================================
    # Delete Subject
    # ==========================================
    @staticmethod
    def delete_subject(subject_id):

        query = """
        DELETE FROM subjects
        WHERE id=%s
        """

        execute_query(
            query,
            (subject_id,)
        )

    # ==========================================
    # Search Subject
    # ==========================================
    @staticmethod
    def search_subject(user_id, keyword):

        query = """
        SELECT *

        FROM subjects

        WHERE

            user_id=%s

            AND

            subject_name LIKE %s

        ORDER BY subject_name
        """

        return fetch_all(
            query,
            (
                user_id,
                "%" + keyword + "%"
            )
        )

    # ==========================================
    # Count Subjects
    # ==========================================
    @staticmethod
    def count_subjects(user_id):

        query = """
        SELECT COUNT(*) AS total

        FROM subjects

        WHERE user_id=%s
        """

        result = fetch_one(
            query,
            (user_id,)
        )

        return result["total"]

    # ==========================================
    # Get High Priority Subjects
    # ==========================================
    @staticmethod
    def high_priority(user_id):

        query = """
        SELECT *

        FROM subjects

        WHERE

            user_id=%s

            AND priority='High'

        ORDER BY subject_name
        """

        return fetch_all(
            query,
            (user_id,)
        )

    # ==========================================
    # Get Difficult Subjects
    # ==========================================
    @staticmethod
    def difficult_subjects(user_id):

        query = """
        SELECT *

        FROM subjects

        WHERE

            user_id=%s

            AND difficulty='Hard'

        ORDER BY subject_name
        """

        return fetch_all(
            query,
            (user_id,)
        )

    # ==========================================
    # Get Subject Names Only
    # ==========================================
    @staticmethod
    def get_subject_names(user_id):

        query = """
        SELECT subject_name

        FROM subjects

        WHERE user_id=%s

        ORDER BY subject_name
        """

        return fetch_all(
            query,
            (user_id,)
        )