from flask import Flask, render_template, request
from datetime import date
from functions import get_locations_daily_weather, get_location, get_context_dict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def weather_app():
    # key, location = get_location("london")
    default_key = "328328"
    default_location = "London"
    weather_dict = get_locations_daily_weather()#default_key
    context_dict = get_context_dict(default_location)

    if request.method == "POST":
        new_location = request.form.get("location")
        #key, location = get_location(new_location)
        location = new_location #fake
        weather_dict = get_locations_daily_weather()#key
        context_dict = get_context_dict(location)
    else:
        pass

    return render_template(
        "index.html",
        current_location=context_dict.get('location'),
        todays_date=context_dict.get('date'),
        max_temp=weather_dict.get('MaxTemp'),
        min_temp=weather_dict.get('MinTemp'),
        summary=weather_dict.get('Summary'),
    )
