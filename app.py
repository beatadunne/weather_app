from flask import Flask, render_template, request, redirect, url_for
from datetime import date
from functions import get_locations_daily_weather, get_location, get_context_dict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def weather_app():
    default_key = "328328"
    default_location = "London"
    weather_dict = get_locations_daily_weather()  # default_key
    context_dict = get_context_dict(default_location)

    if request.method == "POST":
        location = request.form.get("location")
        return redirect(url_for("daily_weather", location=location, code=307))
    else:
        return render_template(
            "index.html",
            current_location=context_dict.get("location"),
            todays_date=context_dict.get("date"),
            max_temp=weather_dict.get("MaxTemp"),
            min_temp=weather_dict.get("MinTemp"),
            summary=weather_dict.get("Summary"),
        )


@app.route("/daily", methods=["GET", "POST"])
def daily_weather():
    # key, location = get_location(location)
    location = request.args.get("location")
    weather_dict = get_locations_daily_weather()  # key
    context_dict = get_context_dict(location)
    return render_template(
        "daily_weather.html",
        current_location=context_dict.get("location"),
        todays_date=context_dict.get("date"),
        max_temp=weather_dict.get("MaxTemp"),
        min_temp=weather_dict.get("MinTemp"),
        summary=weather_dict.get("Summary"),
    )
