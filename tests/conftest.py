import pytest


@pytest.fixture
def example_response():
    return {
        "Headline": {
            "EffectiveDate": "2023-05-04T20:00:00+01:00",
            "EffectiveEpochDate": 1683226800,
            "Severity": 5,
            "Text": "Expect showery weather Thursday evening through Friday afternoon",
            "Category": "rain",
            "EndDate": "2023-05-05T20:00:00+01:00",
            "EndEpochDate": 1683313200,
            "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?lang=en-us",
            "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?lang=en-us",
        },
        "DailyForecasts": [
            {
                "Date": "2023-05-03T07:00:00+01:00",
                "EpochDate": 1683093600,
                "Temperature": {
                    "Minimum": {"Value": 12.0, "Unit": "C", "UnitType": 18},
                    "Maximum": {"Value": 20.0, "Unit": "C", "UnitType": 18},
                },
                "Day": {
                    "Icon": 2,
                    "IconPhrase": "Mostly sunny",
                    "HasPrecipitation": False,
                },
                "Night": {
                    "Icon": 36,
                    "IconPhrase": "Intermittent clouds",
                    "HasPrecipitation": False,
                },
                "Sources": ["AccuWeather"],
                "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=1&lang=en-us",
                "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=1&lang=en-us",
            }
        ],
    }
