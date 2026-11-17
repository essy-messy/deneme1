import json
import urllib.request

url = "https://api.open-meteo.com/v1/forecast?latitude=39.93&longitude=32.86&current=temperature_2m"
cevap = urllib.request.urlopen(url)
veri = json.load(cevap)
print("Ankara şu an:", veri["current"]["temperature_2m"], "°C")
