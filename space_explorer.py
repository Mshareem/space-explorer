import re


import requests

URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

response = requests.get(URL, params={"PqRt7PMpRNrkbtP9TJjbwtRqmMWcpfhPcDGbWMzP": "DEMO_KEY"})
data = response.json()

#print(data[0]["title"])

print("=" * 60)
print("Title:", data[0]["title"])
print("Date: ", data[0]["date"])
print("Image:", data[0]["url"])
print("-" * 60)
print(data[0]["explanation"])
print("=" * 60)

