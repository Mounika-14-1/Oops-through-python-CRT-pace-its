# ==========================================
# app.py
# AI-Powered Study Planner
# Main Flask Application
# ==========================================

from flask import Flask, render_template
from dotenv import load_dotenv
import os


# Import database
from database.db import create_connection


# Import Routes
from routes.auth import auth
from routes.dashboard import dashboard
from routes.planner import planner
from routes.subjects import subjects
from routes.progress import progress
from routes.calendar import calendar



# Load environment variables
load_dotenv()


# ==========================================
# Create Flask App
# ==========================================

app = Flask(__name__)


# Secret Key
app.secret_key = os.getenv(
    "SECRET_KEY",
    "ai_study_planner_secret"
)


# ==========================================
# Register Blueprints
# ==========================================
from routes.calendar import calendar

app.register_blueprint(auth)

app.register_blueprint(dashboard)

app.register_blueprint(planner)

app.register_blueprint(subjects)

app.register_blueprint(progress)

app.register_blueprint(calendar)



# ==========================================
# Home Route
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )



# ==========================================
# Error Handling
# ==========================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404



@app.errorhandler(500)
def internal_error(error):

    return render_template(
        "500.html"
    ), 500



# ==========================================
# Test Database Connection
# ==========================================

@app.route("/test-db")
def test_database():

    try:

        connection = create_connection()

        if connection:

            return "Database Connected Successfully!"

        else:

            return "Database Connection Failed!"

    except Exception as e:

        return str(e)



# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
    

      