# ==========================================
# utils/study_analyzer.py
# AI-Powered Study Planner
# Study Performance Analyzer
# ==========================================

from database.db import fetch_all, fetch_one


class StudyAnalyzer:


    # ==========================================
    # Get Overall Study Statistics
    # ==========================================

    @staticmethod
    def get_study_statistics(user_id):

        query = """

        SELECT

            COUNT(*) AS total_subjects,

            SUM(hours_completed) AS completed_hours,

            SUM(target_hours) AS target_hours,

            AVG(completion_percentage)
            AS average_progress


        FROM progress


        WHERE user_id=%s

        """

        result = fetch_one(
            query,
            (user_id,)
        )


        if result:

            return {

                "total_subjects":
                    result["total_subjects"] or 0,

                "completed_hours":
                    result["completed_hours"] or 0,

                "target_hours":
                    result["target_hours"] or 0,

                "average_progress":
                    round(
                        result["average_progress"] or 0,
                        2
                    )

            }


        return {}



    # ==========================================
    # Subject Performance Analysis
    # ==========================================

    @staticmethod
    def subject_analysis(user_id):

        query = """

        SELECT

            s.subject_name,

            p.hours_completed,

            p.target_hours,

            p.completion_percentage


        FROM progress p


        JOIN subjects s

        ON p.subject_id=s.id


        WHERE p.user_id=%s


        ORDER BY
        p.completion_percentage DESC

        """


        return fetch_all(

            query,

            (user_id,)

        )



    # ==========================================
    # Find Strong Subjects
    # ==========================================

    @staticmethod
    def strong_subjects(user_id):

        query = """

        SELECT

            s.subject_name,

            p.completion_percentage


        FROM progress p


        JOIN subjects s

        ON p.subject_id=s.id


        WHERE

        p.user_id=%s

        AND

        p.completion_percentage >= 80


        ORDER BY
        p.completion_percentage DESC

        """


        return fetch_all(

            query,

            (user_id,)

        )



    # ==========================================
    # Find Weak Subjects
    # ==========================================

    @staticmethod
    def weak_subjects(user_id):

        query = """

        SELECT

            s.subject_name,

            p.completion_percentage


        FROM progress p


        JOIN subjects s

        ON p.subject_id=s.id


        WHERE

        p.user_id=%s

        AND

        p.completion_percentage < 50


        ORDER BY
        p.completion_percentage ASC

        """


        return fetch_all(

            query,

            (user_id,)

        )



    # ==========================================
    # Study Efficiency
    # ==========================================

    @staticmethod
    def study_efficiency(user_id):


        query = """

        SELECT

        SUM(hours_completed)
        AS completed,


        SUM(target_hours)
        AS target


        FROM progress


        WHERE user_id=%s

        """


        result = fetch_one(

            query,

            (user_id,)

        )


        if not result:

            return 0


        if result["target"] == 0:

            return 0


        efficiency = (

            result["completed"]

            /

            result["target"]

        ) * 100


        return round(
            efficiency,
            2
        )



    # ==========================================
    # Generate Study Recommendation
    # ==========================================

    @staticmethod
    def generate_recommendation(user_id):


        weak = StudyAnalyzer.weak_subjects(
            user_id
        )


        strong = StudyAnalyzer.strong_subjects(
            user_id
        )


        recommendations = []


        # Weak Subject Advice

        if weak:


            for subject in weak:

                recommendations.append(

                    f"Increase focus on "
                    f"{subject['subject_name']} "
                    f"because progress is only "
                    f"{subject['completion_percentage']}%."

                )



        # Strong Subject Advice

        if strong:


            recommendations.append(

                "Great work! Continue maintaining "
                "your strong subjects."

            )



        # Default Message

        if not recommendations:


            recommendations.append(

                "Start following your AI-generated "
                "study schedule consistently."

            )


        return recommendations



    # ==========================================
    # Complete Study Analysis Report
    # ==========================================

    @staticmethod
    def complete_analysis(user_id):


        return {


            "statistics":

                StudyAnalyzer.get_study_statistics(
                    user_id
                ),


            "subjects":

                StudyAnalyzer.subject_analysis(
                    user_id
                ),


            "strong_subjects":

                StudyAnalyzer.strong_subjects(
                    user_id
                ),


            "weak_subjects":

                StudyAnalyzer.weak_subjects(
                    user_id
                ),


            "efficiency":

                StudyAnalyzer.study_efficiency(
                    user_id
                ),


            "recommendations":

                StudyAnalyzer.generate_recommendation(
                    user_id
                )

        }