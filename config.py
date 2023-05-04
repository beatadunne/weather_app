""" Config file """

""" Variables needed when connecting to the API """
API_KEY = "dFQky8iYcFxLpRAWb3jTUKyxljIRB2UZ"
API_URL_ROOT = "http://dataservice.accuweather.com"

""" API and variables needed to retrieve Location key """
LOCATION_API = f"{API_URL_ROOT}/locations/v1/cities/search?apikey={API_KEY}"
LOCATION_KEY = "Key"
LOCATION_NAME = "EnglishName"
TOP_RESULT_INDEX = 0

""" API and variables needed to retrieve Weather data """
WEATHER_DAILY_API = f"{API_URL_ROOT}/forecasts/v1/daily/1day/"
WEATHER_FIELDS = {
    "Headline_Text": "Summary",
    "Headline_Category": "WeatherCategory",
    "DailyForecasts_0_Temperature_Minimum_Value": "MinTemp",
    "DailyForecasts_0_Temperature_Maximum_Value": "MaxTemp",
    "DailyForecasts_0_Day_Icon": "DayWeatherIcon",
    "DailyForecasts_0_Day_IconPhrase": "DayWeatherIconPhrase",
}

# @todo: move this into a test file/fixture
""" Example Response used for testing """
EXAMPLE_1DAY_RESPONSE = {
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


EXAMPLE_5DAY_RESPONSE ={
  "Headline": {
    "EffectiveDate": "2023-05-04T14:00:00+01:00",
    "EffectiveEpochDate": 1683205200,
    "Severity": 3,
    "Text": "Showers and thunderstorms around Thursday afternoon through Friday evening",
    "Category": "thunderstorm",
    "EndDate": "2023-05-06T02:00:00+01:00",
    "EndEpochDate": 1683334800,
    "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?unit=c&lang=en-us",
    "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?unit=c&lang=en-us"
  },
  "DailyForecasts": [
    {
      "Date": "2023-05-04T07:00:00+01:00",
      "EpochDate": 1683180000,
      "Temperature": {
        "Minimum": {
          "Value": 11.7,
          "Unit": "C",
          "UnitType": 17
        },
        "Maximum": {
          "Value": 19.4,
          "Unit": "C",
          "UnitType": 17
        }
      },
      "Day": {
        "Icon": 17,
        "IconPhrase": "Partly sunny w/ t-storms",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Night": {
        "Icon": 40,
        "IconPhrase": "Mostly cloudy w/ showers",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Sources": [
        "AccuWeather"
      ],
      "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=1&unit=c&lang=en-us",
      "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=1&unit=c&lang=en-us"
    },
    {
      "Date": "2023-05-05T07:00:00+01:00",
      "EpochDate": 1683266400,
      "Temperature": {
        "Minimum": {
          "Value": 10.4,
          "Unit": "C",
          "UnitType": 17
        },
        "Maximum": {
          "Value": 18,
          "Unit": "C",
          "UnitType": 17
        }
      },
      "Day": {
        "Icon": 16,
        "IconPhrase": "Mostly cloudy w/ t-storms",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Moderate"
      },
      "Night": {
        "Icon": 12,
        "IconPhrase": "Showers",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Sources": [
        "AccuWeather"
      ],
      "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=2&unit=c&lang=en-us",
      "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=2&unit=c&lang=en-us"
    },
    {
      "Date": "2023-05-06T07:00:00+01:00",
      "EpochDate": 1683352800,
      "Temperature": {
        "Minimum": {
          "Value": 11.8,
          "Unit": "C",
          "UnitType": 17
        },
        "Maximum": {
          "Value": 16.2,
          "Unit": "C",
          "UnitType": 17
        }
      },
      "Day": {
        "Icon": 13,
        "IconPhrase": "Mostly cloudy w/ showers",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Night": {
        "Icon": 12,
        "IconPhrase": "Showers",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Sources": [
        "AccuWeather"
      ],
      "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=3&unit=c&lang=en-us",
      "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=3&unit=c&lang=en-us"
    },
    {
      "Date": "2023-05-07T07:00:00+01:00",
      "EpochDate": 1683439200,
      "Temperature": {
        "Minimum": {
          "Value": 10.9,
          "Unit": "C",
          "UnitType": 17
        },
        "Maximum": {
          "Value": 19,
          "Unit": "C",
          "UnitType": 17
        }
      },
      "Day": {
        "Icon": 14,
        "IconPhrase": "Partly sunny w/ showers",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Night": {
        "Icon": 7,
        "IconPhrase": "Cloudy",
        "HasPrecipitation": 'false'
      },
      "Sources": [
        "AccuWeather"
      ],
      "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=4&unit=c&lang=en-us",
      "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=4&unit=c&lang=en-us"
    },
    {
      "Date": "2023-05-08T07:00:00+01:00",
      "EpochDate": 1683525600,
      "Temperature": {
        "Minimum": {
          "Value": 11.2,
          "Unit": "C",
          "UnitType": 17
        },
        "Maximum": {
          "Value": 18.2,
          "Unit": "C",
          "UnitType": 17
        }
      },
      "Day": {
        "Icon": 12,
        "IconPhrase": "Showers",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Night": {
        "Icon": 38,
        "IconPhrase": "Mostly cloudy",
        "HasPrecipitation": 'true',
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light"
      },
      "Sources": [
        "AccuWeather"
      ],
      "MobileLink": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=5&unit=c&lang=en-us",
      "Link": "http://www.accuweather.com/en/gb/london/ec4a-2/daily-weather-forecast/328328?day=5&unit=c&lang=en-us"
    }
  ]
}