import requests
import datetime as dt
import smtplib

my_email = "darknexnguyen2000@gmail.com"
password = "wnolsupvripgehiq"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)



API_KEY = "NY99HTSHEW5WCZLQQ84W65RM6"
parameter = {
    # 'lat':float(14.058324),
    # 'lon':float(108.277199),
    'key':API_KEY,
}
def FtoC_degree(F_degree:float)->float:
    return round((F_degree-32)/1.8,1)

response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/HoChiMinh,VN",params=parameter)
response.raise_for_status()
data = response.json()
current_hour = dt.datetime.now().hour
day = 0
i = current_hour

current_temp_F = data['days'][day]['temp']
current_temp_C = FtoC_degree(current_temp_F)
message=f"Subject: Forecast \n\nHi, today temperature is {current_temp_C}!\nForecast:\n"
for _ in range(24):
    i += 1
    if i == 24:
        day += 1
        i = 0
    message += f"{i}:00: {data['days'][day]['hours'][i]['icon']}\n"
    if data['days'][day]['hours'][i]['icon'] == 'rain':
        will_rain = True

connection.sendmail(from_addr=my_email,to_addrs="darknexnguyen@gmail.com",msg=message)
connection.close()