# ==========================================
# routes/planner.py
# AI-Powered Study Planner
# ==========================================

from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from models.subject_model import Subject
from models.study_plan_model import StudyPlan

planner = Blueprint("planner", __name__)


# ==========================================
# Planner Page
# ==========================================

@planner.route("/planner")
def planner_page():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    subjects = Subject.get_subjects(user_id)

    plans = StudyPlan.get_user_plans(user_id)

    return render_template(
        "planner.html",
        subjects=subjects,
        plans=plans
    )


# ==========================================
# Generate Study Plan
# ==========================================

@planner.route("/generate-plan", methods=["POST"])
def generate_plan():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    subject_id = request.form.get("subject_id")
    plan_type = request.form.get("planType")
    study_hours = request.form.get("studyHours")
    exam_date = request.form.get("examDate")

    # -----------------------------
    # AI Schedule (Temporary)
    # Replace this later with Gemini AI
    # -----------------------------
    ai_schedule = f"""
Study Plan

Plan Type : {plan_type}

Study Hours : {study_hours} Hours

Session 1 :
Read theory

Break : 15 Minutes

Session 2 :
Practice Problems

Session 3 :
Revision

Mock Test before Exam

Good Luck!
"""

    StudyPlan.create_plan(

        user_id=user_id,

        subject_id=subject_id,

        plan_type=plan_type,

        study_hours=study_hours,

        exam_date=exam_date,

        ai_schedule=ai_schedule

    )

    flash("Study Plan Generated Successfully!", "success")

    return redirect(url_for("planner.planner_page"))


# ==========================================
# View Study Plan
# ==========================================

@planner.route("/plan/<int:plan_id>")
def view_plan(plan_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    plan = StudyPlan.get_plan(plan_id)

    return render_template(
        "timetable.html",
        plan=plan
    )


# ==========================================
# Complete Study Plan
# ==========================================

@planner.route("/plan/complete/<int:plan_id>")
def complete_plan(plan_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    StudyPlan.update_status(
        plan_id,
        "Completed"
    )

    flash("Study Plan Completed!", "success")

    return redirect(url_for("planner.planner_page"))


# ==========================================
# Delete Study Plan
# ==========================================

@planner.route("/plan/delete/<int:plan_id>")
def delete_plan(plan_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    StudyPlan.delete_plan(plan_id)

    flash("Study Plan Deleted Successfully!", "success")

    return redirect(url_for("planner.planner_page"))


# ==========================================
# Daily Plans
# ==========================================

@planner.route("/planner/daily")
def daily_plans():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    plans = StudyPlan.get_plans_by_type(
        session["user_id"],
        "Daily"
    )

    return render_template(
        "planner.html",
        plans=plans
    )


# ==========================================
# Weekly Plans
# ==========================================

@planner.route("/planner/weekly")
def weekly_plans():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    plans = StudyPlan.get_plans_by_type(
        session["user_id"],
        "Weekly"
    )

    return render_template(
        "planner.html",
        plans=plans
    )


# ==========================================
# Monthly Plans
# ==========================================

@planner.route("/planner/monthly")
def monthly_plans():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    plans = StudyPlan.get_plans_by_type(
        session["user_id"],
        "Monthly"
    )

    return render_template(
        "planner.html",
        plans=plans
    )