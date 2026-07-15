from flask import Flask, render_template, request
from datetime import date
from age_calculator import calculate_age

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    age = None
    error = None

    if request.method == "POST":

        dob = request.form.get("dob")

        try:
            birth_date = date.fromisoformat(dob)

            if birth_date > date.today():
                error = "Date of birth cannot be in the future."

            else:
                years, months, days = calculate_age(birth_date)

                age = {
                    "years": years,
                    "months": months,
                    "days": days
                }

        except:
            error = "Please enter a valid date."

    return render_template(
        "index.html",
        age=age,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)