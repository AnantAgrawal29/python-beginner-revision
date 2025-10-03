import requests
from datetime import datetime
import smtplib
import time

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_pos = data["iss_position"]
latitude = float(iss_pos['latitude'])
longitude = float(iss_pos['longitude'])

MY_LAT = 26.450486
MY_LONG = 80.191304

# Your position is within +5 or -5 degrees of the ISS position.

params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=params )
response.raise_for_status()
data = response.json()['results']
sunrise = data['sunrise'].split("T")[1].split(":")[0]
sunset = data['sunset'].split("T")[1].split(":")[0]

time_now = datetime.now().hour

# If the ISS is close to my current position and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
my_email = "gigahello2021@gmail.com"
password = "nawhuakvlarshfiq"

while True:
    time.sleep(60)
    if abs(MY_LAT - latitude) <=5 and abs(MY_LONG - longitude) <=5 and (sunset <= time_now or sunrise >= time_now):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="agrawalanant2021@gmail.com",
                msg=f"Look Up",
            )
