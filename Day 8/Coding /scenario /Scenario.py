#Weather App API Handler (Mock)

def fetch_weather(city):
    # Mock response
    data = {
        "Chennai": {"temp": 32, "condition": "Sunny"},
        "Delhi": {"temp": 25, "condition": "Cloudy"}
    }
    return data.get(city, "City not found")

print(fetch_weather("Chennai"))

#Sample Output:{'temp': 32, 'condition': 'Sunny'}

