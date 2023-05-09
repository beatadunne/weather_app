from datetime import date

import pytest
import requests_mock

from config import LOCATION_API, WEATHER_DAILY_API, API_KEY
from functions import (
    get_daily_weather_dict,
    get_context_dict,
    get_five_day_weather_table,
    get_location,
    get_weather_json,
)


# @todo: get_locations_weather


@pytest.mark.parametrize(
    "search_term, expected_location, expected_key",
    [["london", "London", "328328"]],
)
def test_get_location(
    search_term, expected_location, expected_key, locations_api_response
):
    with requests_mock.Mocker() as m:
        m.get(f"{LOCATION_API}&q={search_term}", json=locations_api_response)
        actual_key, actual_location = get_location(search_term)
        assert actual_key == expected_key
        assert actual_location == expected_location


@pytest.mark.parametrize("key, days", [["328328", "1day"]])
def test_get_weather_json_one_day(key, days, example_one_day_response):
    with requests_mock.Mocker() as m:
        m.get(
            f"{WEATHER_DAILY_API}/{days}/{key}?apikey={API_KEY}&metric=true",
            json=example_one_day_response,
        )
        actual_response = get_weather_json(key, days)
        assert actual_response == example_one_day_response


@pytest.mark.parametrize("key, days", [["328328", "5day"]])
def test_get_weather_json_five_day(key, days, example_five_day_response):
    with requests_mock.Mocker() as m:
        m.get(
            f"{WEATHER_DAILY_API}/{days}/{key}?apikey={API_KEY}&metric=true",
            json=example_five_day_response,
        )
        actual_response = get_weather_json(key, days)
        assert actual_response == example_five_day_response


@pytest.mark.parametrize(
    "expected",
    [
        {
            "DayWeatherIcon": 2,
            "DayWeatherIconPhrase": "Mostly sunny",
            "MaxTemp": 20.0,
            "MinTemp": 12.0,
            "Summary": "Expect showery weather Thursday evening through Friday afternoon",
            "WeatherCategory": "rain",
        }
    ],
)
def test_get_daily_weather_dict(expected, example_one_day_response):
    actual = get_daily_weather_dict(example_one_day_response)
    assert actual == expected


def test_get_context_dict():
    actual = get_context_dict("London")
    today = date.today()
    todays_date = today.strftime("%B %d, %Y")
    assert actual == {"location": "London", "date": todays_date}


def test_get_five_day_weather_table(example_five_day_response, expected_html_table):
    actual_html = get_five_day_weather_table(example_five_day_response)
    assert actual_html == expected_html_table
