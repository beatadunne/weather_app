from flask import Flask, render_template, request

from functions import get_locations_daily_weather, get_location

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def weather_app():
    # key, location = get_location("london")
    default_key = "328328"
    location = "London"
    weather_dict = get_locations_daily_weather()#default_key

    if request.method == "POST":
        new_location = request.form.get("location")
        key, location = get_location(new_location)
        weather_dict = get_locations_daily_weather(key)
    else:
        pass

    return render_template(
        "index.html",
        current_location=location,
        max_temp=weather_dict.get('MaxTemp'),
        min_temp=weather_dict.get('MinTemp'),
        summary=weather_dict.get('Summary'),
    )
