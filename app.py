from flask import Flask, render_template, request

from functions import get_locations_daily_weather, get_location

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def weather_app():
    #key, location = get_location("london")
    current_location = "London"
    max_temp, min_temp, summary_text = get_locations_daily_weather()

    if request.method == "POST":
        new_location = request.form.get("location")
        #key, location = get_location(new_location)
    else:
        pass

    return render_template(
        'index.html',
        current_location=current_location,
        max_temp=max_temp,
        min_temp=min_temp,
        summary=summary_text,
    )
