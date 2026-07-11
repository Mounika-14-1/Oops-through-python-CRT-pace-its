# ==========================================
# utils/ai_scheduler.py
# AI-Powered Study Planner
# Google Gemini AI
# ==========================================

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")


class AIStudyScheduler:

    @staticmethod
    def generate_plan(
        subjects,
        plan_type,
        study_hours,
        exam_date,
        learning_style="Balanced"
    ):
        """
        Generate an AI-powered study plan.

        Parameters
        ----------
        subjects : list
            Example:
            ["Python", "Machine Learning", "DBMS"]

        plan_type : str
            Daily / Weekly / Monthly

        study_hours : int or float

        exam_date : str

        learning_style : str
            Balanced / Fast / Intensive
        """

        prompt = f"""
You are an expert academic study planner.

Create a personalized {plan_type} study plan.

Student Details

Subjects:
{', '.join(subjects)}

Available Study Time:
{study_hours} hours per day

Learning Style:
{learning_style}

Exam Date:
{exam_date}

Instructions

1. Divide time equally among subjects.
2. Give exact study timings.
3. Include short breaks.
4. Add revision sessions.
5. Include practice questions.
6. Include mock tests.
7. Give motivational tips.
8. Use tables wherever possible.
9. Return clean Markdown.
"""

        try:

            response = model.generate_content(prompt)

            return response.text

        except Exception as e:

            return f"AI Error: {str(e)}"

    @staticmethod
    def generate_daily_plan(subjects, study_hours):

        return AIStudyScheduler.generate_plan(
            subjects=subjects,
            plan_type="Daily",
            study_hours=study_hours,
            exam_date="Not Specified"
        )

    @staticmethod
    def generate_weekly_plan(
        subjects,
        study_hours,
        exam_date
    ):

        return AIStudyScheduler.generate_plan(
            subjects=subjects,
            plan_type="Weekly",
            study_hours=study_hours,
            exam_date=exam_date
        )

    @staticmethod
    def generate_monthly_plan(
        subjects,
        study_hours,
        exam_date
    ):

        return AIStudyScheduler.generate_plan(
            subjects=subjects,
            plan_type="Monthly",
            study_hours=study_hours,
            exam_date=exam_date
        )