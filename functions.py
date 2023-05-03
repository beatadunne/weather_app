import requests as requests
import pandas as pd
from pandas import DataFrame

from config import LOCATION_API, LOCATION_KEY, LOCATION_NAME, TOP_RESULT_INDEX, WEATHER_DAILY_API, API_KEY, \
    EXAMPLE_RESPONSE


def get_locations_daily_weather():
    weather_json = EXAMPLE_RESPONSE
    max_temp, min_temp = get_temp_table(weather_json)
    summary_text = get_weather_summary(weather_json)
    return max_temp, min_temp, summary_text


def get_location(search_term: str) -> (str, str):
    response = requests.get(f"{LOCATION_API}&q={search_term}")
    if response.status_code == 200:
        top_result = (response.json())[TOP_RESULT_INDEX]
        location_key = top_result[LOCATION_KEY]
        location_name = top_result[LOCATION_NAME]
        return location_key, location_name
    else:
        print("need to sort out error messages")


def get_daily_weather(key: str) -> str:
    response = requests.get(f"{WEATHER_DAILY_API}{key}?apikey={API_KEY}&metric=true")
    if response.status_code == 200:
        return response.json()
    else:
        print("sort errors")


def get_temp_table(weather_json) -> (str, str):
    max_val = weather_json["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
    min_val = weather_json["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
    return max_val, min_val


def get_weather_summary(weather_json) -> str:
    summary = weather_json["Headline"]["Text"]
    return summary
