# ==========================================
# utils/timetable_generator.py
# AI-Powered Study Planner
# Timetable Generator
# ==========================================

from datetime import datetime, timedelta


class TimetableGenerator:


    # ==========================================
    # Generate Daily Timetable
    # ==========================================

    @staticmethod
    def generate_daily_timetable(
        subjects,
        study_hours,
        start_time="09:00",
        break_time=15
    ):

        timetable = []

        current_time = datetime.strptime(
            start_time,
            "%H:%M"
        )

        subject_count = len(subjects)

        if subject_count == 0:
            return []


        # Divide hours among subjects

        hours_per_subject = study_hours / subject_count


        for subject in subjects:

            start = current_time.strftime("%H:%M")


            end_time = current_time + timedelta(
                minutes=int(hours_per_subject * 60)
            )


            end = end_time.strftime("%H:%M")


            timetable.append({

                "subject": subject,

                "start_time": start,

                "end_time": end,

                "activity":
                f"Study {subject}"

            })


            # Add break

            current_time = end_time + timedelta(
                minutes=break_time
            )


        return timetable



    # ==========================================
    # Generate Weekly Timetable
    # ==========================================

    @staticmethod
    def generate_weekly_timetable(
        subjects,
        study_hours,
        start_time="09:00"
    ):

        weekly_plan = {}


        days = [

            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"

        ]


        daily_plan = TimetableGenerator.generate_daily_timetable(
            subjects,
            study_hours,
            start_time
        )


        for day in days:

            weekly_plan[day] = daily_plan


        return weekly_plan



    # ==========================================
    # Generate Monthly Timetable
    # ==========================================

    @staticmethod
    def generate_monthly_timetable(
        subjects,
        study_hours,
        weeks=4
    ):

        monthly_plan = {}


        for week in range(1, weeks + 1):

            monthly_plan[f"Week {week}"] = (

                TimetableGenerator.generate_weekly_timetable(
                    subjects,
                    study_hours
                )

            )


        return monthly_plan



    # ==========================================
    # Convert Timetable To Text
    # ==========================================

    @staticmethod
    def timetable_to_text(timetable):

        output = ""


        if isinstance(timetable, list):

            for item in timetable:

                output += (
                    f"{item['start_time']} - "
                    f"{item['end_time']} : "
                    f"{item['subject']}\n"
                )


        elif isinstance(timetable, dict):

            for day, plans in timetable.items():

                output += f"\n{day}\n"

                for item in plans:

                    output += (
                        f"{item['start_time']} - "
                        f"{item['end_time']} : "
                        f"{item['subject']}\n"
                    )


        return output