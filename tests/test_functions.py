from datetime import date

import pytest

from functions import get_daily_weather_dict, get_context_dict


# @todo: get_locations_daily_weather

# @todo: test_get_location

# @todo: test_get_daily_weather


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
def test_get_daily_weather_dict(expected, example_response):
    actual = get_daily_weather_dict(example_response)
    assert actual == expected


def test_get_context_dict():
    actual = get_context_dict("London")
    today = date.today()
    todays_date = today.strftime("%B %d, %Y")
    assert actual == {"location": "London", "date": todays_date}


# @todo test_get_5day_weather
