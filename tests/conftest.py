import pytest


@pytest.fixture
def example_one_day_response():
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


@pytest.fixture
def example_five_day_response():
    return {
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

@pytest.fixture
def expected_html_table():
  return ('<table border="1" class="dataframe">\n'
 '  <thead>\n'
 '    <tr style="text-align: right;">\n'
 '      <th>Date</th>\n'
 '      <th>Minimum Temperature</th>\n'
 '      <th>Maximum Temperature</th>\n'
 '      <th>Day Summary</th>\n'
 '      <th>Night Summary</th>\n'
 '    </tr>\n'
 '  </thead>\n'
 '  <tbody>\n'
 '    <tr>\n'
 '      <td>2023-05-04</td>\n'
 '      <td>11.7</td>\n'
 '      <td>19.4</td>\n'
 '      <td>Partly sunny w/ t-storms</td>\n'
 '      <td>Mostly cloudy w/ showers</td>\n'
 '    </tr>\n'
 '    <tr>\n'
 '      <td>2023-05-05</td>\n'
 '      <td>10.4</td>\n'
 '      <td>18.0</td>\n'
 '      <td>Mostly cloudy w/ t-storms</td>\n'
 '      <td>Showers</td>\n'
 '    </tr>\n'
 '    <tr>\n'
 '      <td>2023-05-06</td>\n'
 '      <td>11.8</td>\n'
 '      <td>16.2</td>\n'
 '      <td>Mostly cloudy w/ showers</td>\n'
 '      <td>Showers</td>\n'
 '    </tr>\n'
 '    <tr>\n'
 '      <td>2023-05-07</td>\n'
 '      <td>10.9</td>\n'
 '      <td>19.0</td>\n'
 '      <td>Partly sunny w/ showers</td>\n'
 '      <td>Cloudy</td>\n'
 '    </tr>\n'
 '    <tr>\n'
 '      <td>2023-05-08</td>\n'
 '      <td>11.2</td>\n'
 '      <td>18.2</td>\n'
 '      <td>Showers</td>\n'
 '      <td>Mostly cloudy</td>\n'
 '    </tr>\n'
 '  </tbody>\n'
 '</table>')


@pytest.fixture
def locations_api_response():
    return [
        {
            "Version": 1,
            "Key": "328328",
            "Type": "City",
            "Rank": 10,
            "LocalizedName": "London",
            "EnglishName": "London",
            "PrimaryPostalCode": "EC4A 2",
            "Region": {
                "ID": "EUR",
                "LocalizedName": "Europe",
                "EnglishName": "Europe"
            },
            "Country": {
                "ID": "GB",
                "LocalizedName": "United Kingdom",
                "EnglishName": "United Kingdom"
            },
            "AdministrativeArea": {
                "ID": "LND",
                "LocalizedName": "London",
                "EnglishName": "London",
                "Level": 1,
                "LocalizedType": "London Borough",
                "EnglishType": "London Borough",
                "CountryID": "GB"
            },
            "TimeZone": {
                "Code": "BST",
                "Name": "Europe/London",
                "GmtOffset": 1,
                "IsDaylightSaving": 'true',
                "NextOffsetChange": "2023-10-29T01:00:00Z"
            },
            "GeoPosition": {
                "Latitude": 51.514,
                "Longitude": -0.107,
                "Elevation": {
                    "Metric": {
                        "Value": 18,
                        "Unit": "m",
                        "UnitType": 5
                    },
                    "Imperial": {
                        "Value": 59,
                        "Unit": "ft",
                        "UnitType": 0
                    }
                }
            },
            "IsAlias": 'false',
            "SupplementalAdminAreas": [
                {
                    "Level": 0,
                    "LocalizedName": "England",
                    "EnglishName": "England"
                },
                {
                    "Level": 3,
                    "LocalizedName": "Castle Baynard",
                    "EnglishName": "Castle Baynard"
                }
            ],
            "DataSets": [
                "AirQualityCurrentConditions",
                "AirQualityForecasts",
                "Alerts",
                "DailyPollenForecast",
                "ForecastConfidence",
                "FutureRadar",
                "MinuteCast",
                "Radar"
            ]
        },
        {
            "Version": 1,
            "Key": "55489",
            "Type": "City",
            "Rank": 35,
            "LocalizedName": "London",
            "EnglishName": "London",
            "PrimaryPostalCode": "N6B",
            "Region": {
                "ID": "NAM",
                "LocalizedName": "North America",
                "EnglishName": "North America"
            },
            "Country": {
                "ID": "CA",
                "LocalizedName": "Canada",
                "EnglishName": "Canada"
            },
            "AdministrativeArea": {
                "ID": "ON",
                "LocalizedName": "Ontario",
                "EnglishName": "Ontario",
                "Level": 1,
                "LocalizedType": "Province",
                "EnglishType": "Province",
                "CountryID": "CA"
            },
            "TimeZone": {
                "Code": "EDT",
                "Name": "America/Toronto",
                "GmtOffset": -4,
                "IsDaylightSaving": 'true',
                "NextOffsetChange": "2023-11-05T06:00:00Z"
            },
            "GeoPosition": {
                "Latitude": 42.983,
                "Longitude": -81.244,
                "Elevation": {
                    "Metric": {
                        "Value": 247,
                        "Unit": "m",
                        "UnitType": 5
                    },
                    "Imperial": {
                        "Value": 810,
                        "Unit": "ft",
                        "UnitType": 0
                    }
                }
            },
            "IsAlias": 'false',
            "SupplementalAdminAreas": [
                {
                    "Level": 2,
                    "LocalizedName": "Middlesex",
                    "EnglishName": "Middlesex"
                }
            ],
            "DataSets": [
                "AirQualityCurrentConditions",
                "AirQualityForecasts",
                "Alerts",
                "ForecastConfidence",
                "FutureRadar",
                "MinuteCast",
                "Radar"
            ]
        },
        {
            "Version": 1,
            "Key": "333298",
            "Type": "City",
            "Rank": 75,
            "LocalizedName": "London",
            "EnglishName": "London",
            "PrimaryPostalCode": "40741",
            "Region": {
                "ID": "NAM",
                "LocalizedName": "North America",
                "EnglishName": "North America"
            },
            "Country": {
                "ID": "US",
                "LocalizedName": "United States",
                "EnglishName": "United States"
            },
            "AdministrativeArea": {
                "ID": "KY",
                "LocalizedName": "Kentucky",
                "EnglishName": "Kentucky",
                "Level": 1,
                "LocalizedType": "State",
                "EnglishType": "State",
                "CountryID": "US"
            },
            "TimeZone": {
                "Code": "EDT",
                "Name": "America/New_York",
                "GmtOffset": -4,
                "IsDaylightSaving": 'true',
                "NextOffsetChange": "2023-11-05T06:00:00Z"
            },
            "GeoPosition": {
                "Latitude": 37.129,
                "Longitude": -84.083,
                "Elevation": {
                    "Metric": {
                        "Value": 392,
                        "Unit": "m",
                        "UnitType": 5
                    },
                    "Imperial": {
                        "Value": 1285,
                        "Unit": "ft",
                        "UnitType": 0
                    }
                }
            },
            "IsAlias": 'false',
            "SupplementalAdminAreas": [
                {
                    "Level": 2,
                    "LocalizedName": "Laurel",
                    "EnglishName": "Laurel"
                }
            ],
            "DataSets": [
                "AirQualityCurrentConditions",
                "AirQualityForecasts",
                "Alerts",
                "DailyAirQualityForecast",
                "DailyPollenForecast",
                "ForecastConfidence",
                "FutureRadar",
                "MinuteCast",
                "Radar"
            ]
        }]