import requests

URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

response = requests.get(URL, params={"PqRt7PMpRNrkbtP9TJjbwtRqmMWcpfhPcDGbWMzP": "DEMO_KEY"})
data = response.json()

print(data[0]["title"])