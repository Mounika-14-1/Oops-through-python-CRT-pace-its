# ==========================================
# routes/auth.py
# AI-Powered Study Planner
# ==========================================

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import User

auth = Blueprint("auth", __name__)


# ==========================================
# Register
# ==========================================

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        college = request.form.get("college", "")
        course = request.form.get("course", "")
        study_year = request.form.get("study_year", 1)
        daily_goal = request.form.get("daily_goal", 4)

        # Validation
        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("auth.register"))

        # Register user
        success = User.register(
            username,
            email,
            password,
            college,
            course,
            study_year,
            daily_goal
        )

        if success:
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("auth.login"))

        flash("Email already exists.", "danger")
        return redirect(url_for("auth.register"))

    return render_template("register.html")


# ==========================================
# Login
# ==========================================

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.login(email, password)

        if user:

            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["email"] = user["email"]

            flash("Welcome back!", "success")

            return redirect(url_for("dashboard.dashboard_page"))

        flash("Invalid email or password.", "danger")

    return render_template("login.html")


# ==========================================
# Logout
# ==========================================

@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "success")

    return redirect(url_for("auth.login"))


# ==========================================
# Profile
# ==========================================

@auth.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user = User.get_user(session["user_id"])

    return render_template(
        "profile.html",
        user=user
    )


# ==========================================
# Update Profile
# ==========================================

@auth.route("/profile/update", methods=["POST"])
def update_profile():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    User.update_profile(

        session["user_id"],

        request.form.get("username"),

        request.form.get("college"),

        request.form.get("course"),

        request.form.get("study_year"),

        request.form.get("daily_goal"),

        request.form.get("about")

    )

    flash("Profile updated successfully.", "success")

    return redirect(url_for("auth.profile"))