import requests as requests
from flatten_json import flatten

from config import LOCATION_API, LOCATION_KEY, LOCATION_NAME, TOP_RESULT_INDEX, WEATHER_DAILY_API, API_KEY, \
    EXAMPLE_RESPONSE, WEATHER_FIELDS


def get_locations_daily_weather() -> dict: #key: str
    weather_json = EXAMPLE_RESPONSE
    # weather_json = get_daily_weather(key)
    weather_dict = get_weather_dict(weather_json)
    return weather_dict


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


def get_weather_dict(weather_json) -> dict:
    flat_json = flatten(weather_json)
    weather_dict = {WEATHER_FIELDS[old_key]: value for (old_key, value) in flat_json.items() if old_key in WEATHER_FIELDS}
    return weather_dict
