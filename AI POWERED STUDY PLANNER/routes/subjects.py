# ==========================================
# routes/subjects.py
# AI-Powered Study Planner
# ==========================================

from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from models.subject_model import Subject

subjects = Blueprint("subjects", __name__)


# ==========================================
# View All Subjects
# ==========================================

@subjects.route("/subjects")
def subjects_page():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    subject_list = Subject.get_subjects(user_id)

    return render_template(
        "subject.html",
        subjects=subject_list
    )


# ==========================================
# Add Subject
# ==========================================

@subjects.route("/subjects/add", methods=["POST"])
def add_subject():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    subject_name = request.form.get("subject_name")
    difficulty = request.form.get("difficulty")
    priority = request.form.get("priority")

    if not subject_name:
        flash("Subject name is required.", "danger")
        return redirect(url_for("subjects.subjects_page"))

    Subject.add_subject(
        user_id,
        subject_name,
        difficulty,
        priority
    )

    flash("Subject added successfully!", "success")

    return redirect(url_for("subjects.subjects_page"))


# ==========================================
# Edit Subject Page
# ==========================================

@subjects.route("/subjects/edit/<int:subject_id>")
def edit_subject(subject_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    subject = Subject.get_subject(subject_id)

    if not subject:
        flash("Subject not found.", "danger")
        return redirect(url_for("subjects.subjects_page"))

    return render_template(
        "edit_subject.html",
        subject=subject
    )


# ==========================================
# Update Subject
# ==========================================

@subjects.route("/subjects/update/<int:subject_id>", methods=["POST"])
def update_subject(subject_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    Subject.update_subject(
        subject_id,
        request.form.get("subject_name"),
        request.form.get("difficulty"),
        request.form.get("priority")
    )

    flash("Subject updated successfully!", "success")

    return redirect(url_for("subjects.subjects_page"))


# ==========================================
# Delete Subject
# ==========================================

@subjects.route("/subjects/delete/<int:subject_id>")
def delete_subject(subject_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    Subject.delete_subject(subject_id)

    flash("Subject deleted successfully!", "success")

    return redirect(url_for("subjects.subjects_page"))


# ==========================================
# Search Subject
# ==========================================

@subjects.route("/subjects/search", methods=["GET"])
def search_subject():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    keyword = request.args.get("keyword", "").strip()

    results = Subject.search_subject(
        session["user_id"],
        keyword
    )

    return render_template(
        "subject.html",
        subjects=results,
        keyword=keyword
    )