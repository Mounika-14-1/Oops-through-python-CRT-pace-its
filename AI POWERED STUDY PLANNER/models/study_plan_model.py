# ==========================================
# models/study_plan_model.py
# AI-Powered Study Planner
# ==========================================

from database.db import fetch_one, fetch_all, execute_insert, execute_query


class StudyPlan:

    # ==========================================
    # Create Study Plan
    # ==========================================
    @staticmethod
    def create_plan(
        user_id,
        subject_id,
        plan_type,
        study_hours,
        exam_date,
        ai_schedule
    ):

        query = """
        INSERT INTO study_plans
        (
            user_id,
            subject_id,
            plan_type,
            study_hours,
            exam_date,
            ai_schedule
        )
        VALUES
        (
            %s,
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
                plan_type,
                study_hours,
                exam_date,
                ai_schedule
            )
        )

    # ==========================================
    # Get Plan By ID
    # ==========================================
    @staticmethod
    def get_plan(plan_id):

        query = """
        SELECT
            sp.*,
            s.subject_name
        FROM study_plans sp
        JOIN subjects s
        ON sp.subject_id = s.id
        WHERE sp.id = %s
        """

        return fetch_one(query, (plan_id,))

    # ==========================================
    # Get All Plans of User
    # ==========================================
    @staticmethod
    def get_user_plans(user_id):

        query = """
        SELECT
            sp.*,
            s.subject_name
        FROM study_plans sp
        JOIN subjects s
        ON sp.subject_id = s.id

        WHERE sp.user_id = %s

        ORDER BY sp.created_at DESC
        """

        return fetch_all(query, (user_id,))

    # ==========================================
    # Get Plans By Type
    # ==========================================
    @staticmethod
    def get_plans_by_type(user_id, plan_type):

        query = """
        SELECT
            sp.*,
            s.subject_name

        FROM study_plans sp

        JOIN subjects s

        ON sp.subject_id = s.id

        WHERE

            sp.user_id = %s

            AND

            sp.plan_type = %s

        ORDER BY sp.created_at DESC
        """

        return fetch_all(query, (user_id, plan_type))

    # ==========================================
    # Update Study Plan
    # ==========================================
    @staticmethod
    def update_plan(
        plan_id,
        study_hours,
        exam_date,
        ai_schedule,
        status
    ):

        query = """
        UPDATE study_plans

        SET

            study_hours = %s,
            exam_date = %s,
            ai_schedule = %s,
            status = %s

        WHERE id = %s
        """

        execute_query(
            query,
            (
                study_hours,
                exam_date,
                ai_schedule,
                status,
                plan_id
            )
        )

    # ==========================================
    # Update Plan Status
    # ==========================================
    @staticmethod
    def update_status(plan_id, status):

        query = """
        UPDATE study_plans

        SET status = %s

        WHERE id = %s
        """

        execute_query(query, (status, plan_id))

    # ==========================================
    # Delete Plan
    # ==========================================
    @staticmethod
    def delete_plan(plan_id):

        query = """
        DELETE FROM study_plans
        WHERE id = %s
        """

        execute_query(query, (plan_id,))

    # ==========================================
    # Count User Plans
    # ==========================================
    @staticmethod
    def count_plans(user_id):

        query = """
        SELECT COUNT(*) AS total

        FROM study_plans

        WHERE user_id = %s
        """

        result = fetch_one(query, (user_id,))

        return result["total"]

    # ==========================================
    # Count Completed Plans
    # ==========================================
    @staticmethod
    def completed_plans(user_id):

        query = """
        SELECT COUNT(*) AS total

        FROM study_plans

        WHERE

            user_id = %s

            AND

            status = 'Completed'
        """

        result = fetch_one(query, (user_id,))

        return result["total"]

    # ==========================================
    # Total Study Hours
    # ==========================================
    @staticmethod
    def total_hours(user_id):

        query = """
        SELECT
            IFNULL(SUM(study_hours),0) AS hours

        FROM study_plans

        WHERE user_id = %s
        """

        result = fetch_one(query, (user_id,))

        return result["hours"]

    # ==========================================
    # Latest Study Plan
    # ==========================================
    @staticmethod
    def latest_plan(user_id):

        query = """
        SELECT
            sp.*,
            s.subject_name

        FROM study_plans sp

        JOIN subjects s

        ON sp.subject_id = s.id

        WHERE sp.user_id = %s

        ORDER BY sp.created_at DESC

        LIMIT 1
        """

        return fetch_one(query, (user_id,))