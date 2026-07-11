# ==========================================
# routes/progress.py
# AI-Powered Study Planner
# ==========================================

from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from models.progress_model import Progress
from models.subject_model import Subject

progress = Blueprint("progress", __name__)


# ==========================================
# Progress Dashboard
# ==========================================

@progress.route("/progress")
def progress_page():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    progress_list = Progress.get_user_progress(user_id)

    summary = Progress.dashboard_summary(user_id)

    return render_template(
        "progress.html",
        progress_list=progress_list,
        summary=summary
    )


# ==========================================
# Add Progress Record
# ==========================================

@progress.route("/progress/add", methods=["POST"])
def add_progress():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    subject_id = request.form.get("subject_id")
    target_hours = float(request.form.get("target_hours", 0))

    Progress.create_progress(
        user_id=user_id,
        subject_id=subject_id,
        hours_completed=0,
        target_hours=target_hours,
        completion_percentage=0
    )

    flash("Progress record created successfully!", "success")

    return redirect(url_for("progress.progress_page"))


# ==========================================
# Update Progress
# ==========================================

@progress.route("/progress/update/<int:progress_id>", methods=["POST"])
def update_progress(progress_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    hours_completed = float(request.form.get("hours_completed", 0))
    target_hours = float(request.form.get("target_hours", 0))

    percentage = 0

    if target_hours > 0:
        percentage = min(
            round((hours_completed / target_hours) * 100),
            100
        )

    Progress.update_progress(
        progress_id,
        hours_completed,
        target_hours,
        percentage
    )

    flash("Progress updated successfully!", "success")

    return redirect(url_for("progress.progress_page"))


# ==========================================
# Add Study Hours
# ==========================================

@progress.route("/progress/add-hours/<int:progress_id>", methods=["POST"])
def add_hours(progress_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    hours = float(request.form.get("hours", 0))

    Progress.add_study_hours(progress_id, hours)

    flash("Study hours added successfully!", "success")

    return redirect(url_for("progress.progress_page"))


# ==========================================
# Delete Progress
# ==========================================

@progress.route("/progress/delete/<int:progress_id>")
def delete_progress(progress_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    Progress.delete_progress(progress_id)

    flash("Progress deleted successfully!", "success")

    return redirect(url_for("progress.progress_page"))


# ==========================================
# Subject-wise Progress
# ==========================================

@progress.route("/progress/subject/<int:subject_id>")
def subject_progress(subject_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    subject = Subject.get_subject(subject_id)

    progress_data = Progress.get_progress(subject_id)

    return render_template(
        "progress.html",
        subject=subject,
        progress_data=progress_data
    )


# ==========================================
# Dashboard Summary API
# ==========================================

@progress.route("/progress/summary")
def progress_summary():

    if "user_id" not in session:
        return {"success": False}

    summary = Progress.dashboard_summary(session["user_id"])

    return {
        "success": True,
        "overall_progress": summary["overall_progress"],
        "completed_hours": summary["completed_hours"],
        "target_hours": summary["target_hours"],
        "best_subject": summary["best_subject"],
        "weakest_subject": summary["weakest_subject"]
    }