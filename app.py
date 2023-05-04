from flask import Flask, render_template, request, redirect, url_for

from config import EXAMPLE_5DAY_RESPONSE
from functions import get_locations_daily_weather, get_location, get_context_dict, get_5day_weather

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def weather_app():
    if request.method == "POST":
        location = request.form.get("location")
        return redirect(url_for("daily_weather", location=location, code=307))
    else:
        return render_template(
            "index.html")


@app.route("/london-1-day", methods=["GET", "POST"])
def london_daily():
    weather_dict = get_locations_daily_weather()  # key328328
    context_dict = get_context_dict("London")
    return render_template(
        "daily_weather.html",
        current_location="London",
        todays_date=context_dict.get("date"),
        max_temp=weather_dict.get("MaxTemp"),
        min_temp=weather_dict.get("MinTemp"),
        summary=weather_dict.get("Summary"),
    )


@app.route("/daily", methods=["GET", "POST"])
def daily_weather():
    location = request.args.get("location")
    # key, location = get_location(location)
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


@app.route("/5-day", methods=["GET", "POST"])
def five_day_weather():
    location = request.args.get("name")
    weather_table = get_5day_weather(EXAMPLE_5DAY_RESPONSE)
    return render_template("five_day_weather.html", location=location, tables=[weather_table])
