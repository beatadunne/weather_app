import logging
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
    WEATHER_FIELDS,
)

logger = logging.getLogger()


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
        logger.warning("Location cannot be found")


def get_weather_json(key: str, days: str) -> str:
    """
    Function to retrieve the weather forecast from the AccuWeather API, for a given timespan option.
    Metric = true returns values in Centigrade rather than Fahrenheit.
    :param key: Location key
    :param days: number of days (either 1day or 5day)
    :return: response JSON
    """
    response = requests.get(
        f"{WEATHER_DAILY_API}/{days}/{key}?apikey={API_KEY}&metric=true"
    )
    if response.status_code == 200:
        return response.json()
    else:
        logger.warning("Weather cannot be retrieved")


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
    """
    Function formats the weather json into a table with the features we require
    :param weather_json: response JSON from API (Note: there is no typehint for JSON)
    :return: html of table
    """
    weather_table = pd.json_normalize(weather_json["DailyForecasts"])
    weather_table["Date"] = weather_table["Date"].str[:10]
    selector = {
        "Date": "Date",
        "Temperature.Minimum.Value": "Minimum Temperature",
        "Temperature.Maximum.Value": "Maximum Temperature",
        "Day.IconPhrase": "Day Summary",
        "Night.IconPhrase": "Night Summary",
    }
    small_table = weather_table.rename(columns=selector)[[*selector.values()]]
    return small_table.to_html(index=False)
