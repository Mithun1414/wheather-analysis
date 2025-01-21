import streamlit as st
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Function to get weather data
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Streamlit App
def weather_app():
    st.title('Weather Data Analysis Dashboard')
    
    # Get the user's input for city
    city = st.text_input('Enter the city name', 'New York')
    
    # Enter your OpenWeatherMap API key here
    api_key = '4b033004659dd55cb0c45b42759e5a4f'
    
    if city:
        # Fetch data from OpenWeatherMap API
        data = get_weather_data(city, api_key)
        
        if data.get("cod") != 200:
            st.error("City not found or there was an error with the API request.")
        else:
            # Extract relevant data
            main_data = data['main']
            weather_data = data['weather'][0]
            wind_data = data['wind']
            date_time = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            
            # Display current weather data
            st.header(f"Weather in {city} ({date_time})")
            st.write(f"Weather: {weather_data['description'].capitalize()}")
            st.write(f"Temperature: {main_data['temp']}°C")
            st.write(f"Humidity: {main_data['humidity']}%")
            st.write(f"Pressure: {main_data['pressure']} hPa")
            st.write(f"Wind Speed: {wind_data['speed']} m/s")
            
            # Temperature Plot (Simple Example)
            fig, ax = plt.subplots()
            ax.barh([0], [main_data['temp']], color='skyblue')
            ax.set_xlim(0, 40)
            ax.set_title('Current Temperature')
            ax.set_yticks([0])
            ax.set_yticklabels([city])
            st.pyplot(fig)
            
            # Additional: Display more data like sunrise/sunset or forecast
            st.subheader("Additional Info")
            st.write(f"Sunrise: {datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')}")
            st.write(f"Sunset: {datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')}")

# Run the app
if __name__ == "__main__":
    weather_app()
