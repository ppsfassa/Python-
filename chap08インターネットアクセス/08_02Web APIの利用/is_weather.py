import requests
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = { 'city': '130010' }#①
weather_data = requests.get(url, params=payload).json()#②
for weather in weather_data['forecasts']:#③
    print(
        weather['dateLabel']
        + 'の天気は'
        + weather['telop']
    )
