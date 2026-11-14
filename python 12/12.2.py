import requests

api_key = "OMA_API_AVAIN"

paikka = input("Anna paikkakunta: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&appid={api_key}&units=metric&lang=fi"

vastaus = requests.get(url)
tiedot = vastaus.json()

print("Sää:", tiedot["weather"][0]["description"])
print("Lämpötila:", tiedot["main"]["temp"], "°C")