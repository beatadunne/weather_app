from datetime import date

import pandas as pd
import requests as requests
from flatten_json import flatten

from config import (
    LOCATION_API,
    LOCATION_KEY,
    LOCATION_NAME,
    TOP_RESULT_INDEX,
    WEATHER_DAILY_API,
    API_KEY,
    EXAMPLE_1DAY_RESPONSE,
    WEATHER_FIELDS, EXAMPLE_5DAY_RESPONSE,
)


def get_locations_weather(num_of_days: str, key: str) -> dict or pd.DataFrame:  # key: str
    """
    Function to collect the weather for 1 day, and extract the useful information.
    :key: Location key found using the search term
    :return: weather dictionary containing required fields
    """
    if num_of_days == "1 day":
        #weather_json = EXAMPLE_1DAY_RESPONSE
        weather_json = get_daily_weather_json(key)
        return get_daily_weather_dict(weather_json)
    elif num_of_days == "5 days":
        #weather_json = EXAMPLE_5DAY_RESPONSE
        weather_json = get_five_day_weather_json(key)
        return get_five_day_weather_table(weather_json)
    else:
        print("need to sort errors")


def get_location(search_term: str) -> (str, str):
    """
    Function to get the location key and full English name from the search term provided.
    The location key is needed to retrieve weather information.
    :param search_term: String place-name that has been searched for
    :return: location key and location name
    """
    response = requests.get(f"{LOCATION_API}&q={search_term}")
    if response.status_code == 200:
        top_result = (response.json())[TOP_RESULT_INDEX]
        location_key = top_result[LOCATION_KEY]
        location_name = top_result[LOCATION_NAME]
        return location_key, location_name
    else:
        print("need to sort out error messages")


def get_daily_weather_json(key: str) -> str:
    """
    Function to retrieve the 1-day weather forecast from the AccuWeather API.
    Metric = true returns values in Centigrade rather than Fahrenheit.
    :param key: Location key
    :return: response JSON
    """
    response = requests.get(f"{WEATHER_DAILY_API}/1day/{key}?apikey={API_KEY}&metric=true")
    if response.status_code == 200:
        return response.json()
    else:
        print("sort errors")


def get_five_day_weather_json(key: str) -> str:
    response = requests.get(f"{WEATHER_DAILY_API}/5day/{key}?apikey={API_KEY}&metric=true")
    if response.status_code == 200:
        return response.json()
    else:
        print("sort errors")


def get_daily_weather_dict(weather_json) -> dict[str, str]:
    """
    Function to process API response JSON by flattening and extracting the necessary fields.
    The fields needed can be updated via config.py
    :param weather_json: response JSON from API
    :return: dictionary of required fields and values
    """
    flat_json = flatten(weather_json)
    weather_dict = {
        WEATHER_FIELDS[old_key]: value
        for (old_key, value) in flat_json.items()
        if old_key in WEATHER_FIELDS
    }
    return weather_dict


def get_context_dict(location: str) -> dict:
    """
    Function formats the location and current date into a dictionary
    :param location: formal name of location retrieved from API
    :return: dictionary of location and date
    """
    today = date.today()
    context = {"location": location, "date": today.strftime("%B %d, %Y")}
    return context


def get_five_day_weather_table(weather_json) -> str:
    weather_table = pd.json_normalize(weather_json["DailyForecasts"])
    weather_table["Date"] = weather_table["Date"].str[:10]
    selector = {
        "Date": "Date",
        "Temperature.Minimum.Value": "Minimum Temperature",
        "Temperature.Maximum.Value": "Maximum Temperature",
        "Day.IconPhrase": "Day Summary",
        "Night.IconPhrase": "Night Summary"
    }
    small_table = weather_table.rename(columns=selector)[[*selector.values()]]
    small_table.set_index("Date", inplace=True)
    return small_table.to_html()
