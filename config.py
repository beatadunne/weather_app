API_KEY = "dFQky8iYcFxLpRAWb3jTUKyxljIRB2UZ"
API_URL_ROOT = "http://dataservice.accuweather.com"

LOCATION_API = f"{API_URL_ROOT}/locations/v1/cities/search?apikey={API_KEY}"

LOCATION_KEY = "Key"
LOCATION_NAME = "EnglishName"
TOP_RESULT_INDEX = 0

WEATHER_DAILY_API = f"{API_URL_ROOT}/forecasts/v1/daily/1day/"

WEATHER_FIELDS = {
    "Headline_Text": "Summary",
    "Headline_Category": "WeatherCategory",
    "DailyForecasts_0_Temperature_Minimum_Value": "MinTemp",
    "DailyForecasts_0_Temperature_Maximum_Value": "MaxTemp",
    "DailyForecasts_0_Day_Icon": "DayWeatherIcon",
    "DailyForecasts_0_Day_IconPhrase": "DayWeatherIconPhrase",
}

EXAMPLE_RESPONSE = {
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
            "Day": {"Icon": 2, "IconPhrase": "Mostly sunny", "HasPrecipitation": False},
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
