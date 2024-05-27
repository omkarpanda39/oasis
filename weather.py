import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
    else:
        return None

def main():
    api_key = '6c96001bb898254a368d432c244e2bf2'  # Replace with your actual API key
    location = input("Enter the city name or ZIP code: ")
    
    weather = get_weather(api_key, location)
    
    if weather:
        print(f"Weather in {location}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['description'].capitalize()}")
    else:
        print("Sorry, couldn't fetch the weather data. Please check the location and try again.")

if __name__ == "__main__":
    main()

