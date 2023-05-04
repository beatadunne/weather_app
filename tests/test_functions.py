import pytest

from functions import get_weather_dict


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
def test_get_weather_dict(expected, example_response):
    actual = get_weather_dict(example_response)
    assert actual == expected
