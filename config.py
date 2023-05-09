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
WEATHER_DAILY_API = f"{API_URL_ROOT}/forecasts/v1/daily"
WEATHER_FIELDS = {
    "Headline_Text": "Summary",
    "Headline_Category": "WeatherCategory",
    "DailyForecasts_0_Temperature_Minimum_Value": "MinTemp",
    "DailyForecasts_0_Temperature_Maximum_Value": "MaxTemp",
    "DailyForecasts_0_Day_Icon": "DayWeatherIcon",
    "DailyForecasts_0_Day_IconPhrase": "DayWeatherIconPhrase",
}

""" Variables to specify timespan """
ONE_DAY = "1day"
FIVE_DAY = "5day"
