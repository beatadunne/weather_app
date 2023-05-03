from flask import Flask, render_template

from functions import get_locations_daily_weather, get_location

app = Flask(__name__)


@app.route('/')
def weather_app():
    #key, location = get_location("london")
    location = "London"
    max_temp, min_temp, summary_text = get_locations_daily_weather()
    return render_template(
        'index.html',
        current_location=location,
        max_temp=max_temp,
        min_temp=min_temp,
        summary=summary_text)
