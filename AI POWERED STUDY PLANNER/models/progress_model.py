# ==========================================
# models/progress_model.py
# AI-Powered Study Planner
# ==========================================

from database.db import fetch_one, fetch_all, execute_insert, execute_query


class Progress:

    # ==========================================
    # Create Progress Record
    # ==========================================
    @staticmethod
    def create_progress(
        user_id,
        subject_id,
        hours_completed=0,
        target_hours=0,
        completion_percentage=0
    ):

        query = """
        INSERT INTO progress
        (
            user_id,
            subject_id,
            hours_completed,
            target_hours,
            completion_percentage
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
                subject_id,
                hours_completed,
                target_hours,
                completion_percentage
            )
        )

    # ==========================================
    # Get Progress by Subject
    # ==========================================
    @staticmethod
    def get_progress(subject_id):

        query = """
        SELECT *
        FROM progress
        WHERE subject_id=%s
        """

        return fetch_one(query, (subject_id,))

    # ==========================================
    # Get All Progress of User
    # ==========================================
    @staticmethod
    def get_user_progress(user_id):

        query = """
        SELECT
            p.*,
            s.subject_name

        FROM progress p

        JOIN subjects s

        ON p.subject_id = s.id

        WHERE p.user_id=%s

        ORDER BY s.subject_name
        """

        return fetch_all(query, (user_id,))

    # ==========================================
    # Update Progress
    # ==========================================
    @staticmethod
    def update_progress(
        progress_id,
        hours_completed,
        target_hours,
        completion_percentage
    ):

        query = """
        UPDATE progress

        SET

            hours_completed=%s,
            target_hours=%s,
            completion_percentage=%s

        WHERE id=%s
        """

        execute_query(
            query,
            (
                hours_completed,
                target_hours,
                completion_percentage,
                progress_id
            )
        )

    # ==========================================
    # Add Study Hours
    # ==========================================
    @staticmethod
    def add_study_hours(progress_id, additional_hours):

        progress = fetch_one(
            """
            SELECT *
            FROM progress
            WHERE id=%s
            """,
            (progress_id,)
        )

        if not progress:
            return False

        new_hours = progress["hours_completed"] + additional_hours

        target = progress["target_hours"]

        percentage = 0

        if target > 0:
            percentage = min(
                int((new_hours / target) * 100),
                100
            )

        execute_query(
            """
            UPDATE progress

            SET

                hours_completed=%s,
                completion_percentage=%s

            WHERE id=%s
            """,
            (
                new_hours,
                percentage,
                progress_id
            )
        )

        return True

    # ==========================================
    # Delete Progress
    # ==========================================
    @staticmethod
    def delete_progress(progress_id):

        execute_query(
            """
            DELETE FROM progress
            WHERE id=%s
            """,
            (progress_id,)
        )

    # ==========================================
    # Overall Completion %
    # ==========================================
    @staticmethod
    def overall_progress(user_id):

        result = fetch_one(
            """
            SELECT
                AVG(completion_percentage) AS average_progress

            FROM progress

            WHERE user_id=%s
            """,
            (user_id,)
        )

        if result["average_progress"] is None:
            return 0

        return round(result["average_progress"])

    # ==========================================
    # Total Hours Completed
    # ==========================================
    @staticmethod
    def total_hours(user_id):

        result = fetch_one(
            """
            SELECT
                IFNULL(SUM(hours_completed),0) AS total

            FROM progress

            WHERE user_id=%s
            """,
            (user_id,)
        )

        return result["total"]

    # ==========================================
    # Total Target Hours
    # ==========================================
    @staticmethod
    def target_hours(user_id):

        result = fetch_one(
            """
            SELECT
                IFNULL(SUM(target_hours),0) AS total

            FROM progress

            WHERE user_id=%s
            """,
            (user_id,)
        )

        return result["total"]

    # ==========================================
    # Highest Progress Subject
    # ==========================================
    @staticmethod
    def best_subject(user_id):

        query = """
        SELECT

            s.subject_name,
            p.completion_percentage

        FROM progress p

        JOIN subjects s

        ON p.subject_id=s.id

        WHERE p.user_id=%s

        ORDER BY p.completion_percentage DESC

        LIMIT 1
        """

        return fetch_one(query, (user_id,))

    # ==========================================
    # Lowest Progress Subject
    # ==========================================
    @staticmethod
    def weakest_subject(user_id):

        query = """
        SELECT

            s.subject_name,
            p.completion_percentage

        FROM progress p

        JOIN subjects s

        ON p.subject_id=s.id

        WHERE p.user_id=%s

        ORDER BY p.completion_percentage ASC

        LIMIT 1
        """

        return fetch_one(query, (user_id,))

    # ==========================================
    # Dashboard Summary
    # ==========================================
    @staticmethod
    def dashboard_summary(user_id):

        return {

            "overall_progress":
                Progress.overall_progress(user_id),

            "completed_hours":
                Progress.total_hours(user_id),

            "target_hours":
                Progress.target_hours(user_id),

            "best_subject":
                Progress.best_subject(user_id),

            "weakest_subject":
                Progress.weakest_subject(user_id)

        }