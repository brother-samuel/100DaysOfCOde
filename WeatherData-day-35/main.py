import requests
import smtplib

MY_LAT = 48.613122 
MY_LONG = 14.308521 
EMAIL = "akandreios@gmail.com"
PSWRD = "qphqfjwgosatsivg"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": "c303c26c7deadd7f963165dbdfd9ad1d",
    "cnt": 4,
    "units": "metric"
}

def get_forecast():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    weather_data = response.json()
   
    # print(weather_data["list"][0]["weather"][0]["id"])
    will_rain = False
    for item in weather_data["list"]:
        if item["weather"][0]["id"] < 600:
            will_rain = True
    
    if will_rain:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PSWRD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="uncle.underhill@gmail.com",
                msg=f"Subject: Good morning!\n\n "
                    f"It would be advisable to take your umbrella with you today...")
            
get_forecast()