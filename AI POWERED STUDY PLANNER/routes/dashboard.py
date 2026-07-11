# ==========================================
# routes/dashboard.py
# AI-Powered Study Planner
# ==========================================

from flask import Blueprint, render_template, session, redirect, url_for

from models.user_model import User
from models.study_plan_model import StudyPlan
from models.progress_model import Progress
from models.subject_model import Subject

dashboard = Blueprint("dashboard", __name__)


# ==========================================
# Dashboard
# ==========================================

@dashboard.route("/dashboard")
def dashboard_page():

    # User must be logged in
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    # Get logged-in user
    user = User.get_user(user_id)

    # Dashboard Statistics
    total_subjects = Subject.count_subjects(user_id)

    total_plans = StudyPlan.count_plans(user_id)

    completed_plans = StudyPlan.completed_plans(user_id)

    total_hours = StudyPlan.total_hours(user_id)

    overall_progress = Progress.overall_progress(user_id)

    latest_plan = StudyPlan.latest_plan(user_id)

    plans = StudyPlan.get_user_plans(user_id)

    summary = Progress.dashboard_summary(user_id)

    return render_template(

        "dashboard.html",

        user=user,

        username=user["username"],

        total_subjects=total_subjects,

        total_plans=total_plans,

        completed_plans=completed_plans,

        total_hours=total_hours,

        overall_progress=overall_progress,

        latest_plan=latest_plan,

        plans=plans,

        summary=summary

    )


# ==========================================
# Dashboard Statistics API
# ==========================================

@dashboard.route("/dashboard/stats")
def dashboard_stats():

    if "user_id" not in session:
        return {
            "success": False
        }

    user_id = session["user_id"]

    return {

        "success": True,

        "subjects": Subject.count_subjects(user_id),

        "plans": StudyPlan.count_plans(user_id),

        "completed": StudyPlan.completed_plans(user_id),

        "hours": StudyPlan.total_hours(user_id),

        "progress": Progress.overall_progress(user_id)

    }