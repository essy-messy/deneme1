import json
import urllib.request
url = "https://api.open-meteo.com/v1/forecast?latitude=39.93&longitude=32.86&current=temperature_2m"
with urllib.request.urlopen (url) as r:
 veri = json.load(r)
  print("Ankara şu an:", veri["current"]["temperature_2m"], "°C")
