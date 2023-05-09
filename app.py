import logging

from flask import Flask, render_template, request, redirect, url_for

from config import ONE_DAY, FIVE_DAY
from functions import (
    get_context_dict,
    get_location,
    get_weather_json,
    get_daily_weather_dict,
    get_five_day_weather_table,
)

logging.basicConfig(filename="record.log", level=logging.DEBUG)
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def weather_app():
    if request.method == "POST":
        location = request.form.get("location")
        duration = request.form.get("days")
        app.logger.debug(f"{duration} weather for {location}")
        if duration == "1 day":
            return redirect(url_for("daily_weather", location=location, code=307))
        if duration == "5 days":
            return redirect(url_for("five_day_weather", location=location, code=307))
    else:
        return render_template("index.html")


@app.route("/daily", methods=["GET", "POST"])
def daily_weather():
    location = request.args.get("location")
    key, location = get_location(location)
    weather_info = get_weather_json(key, ONE_DAY)
    weather_dict = get_daily_weather_dict(weather_info)
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
    location = request.args.get("location")
    key, location = get_location(location)
    weather_info = get_weather_json(key, FIVE_DAY)
    weather_table = get_five_day_weather_table(weather_info)
    return render_template(
        "five_day_weather.html", location=location, tables=[weather_table]
    )
