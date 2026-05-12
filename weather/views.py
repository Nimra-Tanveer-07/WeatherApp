from django.shortcuts import render
import requests

# Create your views here.
API_KEY = "4b972341e30cff2a0ee749abba915d96"

def home(request):
    weather_data = None 
    forecast_list = []
    current_url = None

    if request.method == "POST":
        location = request.POST.get('location', '').strip()
        
        if location:
            if location.isdigit():
                current_url = f"https://api.openweathermap.org/data/2.5/weather?zip={location},PK&appid={API_KEY}&units=metric"
                forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={location},PK&appid={API_KEY}&units=metric"
            else:
                current_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric" 
                forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
        #getting current upto 3 hous weather data 
        if current_url:

            current_response = requests.get(current_url)
            forecast_response = requests.get(forecast_url)


            if current_response.status_code == 200:
                
                current_data = current_response.json()
                forecast_data = forecast_response.json()

                #show current data
                weather_data = {
                    'location' : location,
                    'temperature' : current_data['main']['temp'],
                    'description' : current_data['weather'][0]['description'],
                    'icon' : current_data['weather'][0]['icon']
                }

                #And Also show forecast data
                forecasts = forecast_data['list']

                for forecast in forecasts:
                    if "12:00:00" in forecast['dt_txt']:
                        forecast_list.append(
                            {
                                'date' : forecast['dt_txt'],
                                'temperature' : forecast['main']['temp'],
                                'description' : forecast['weather'][0]['description'],
                                'icon' : forecast['weather'][0]['icon'],

                            }
                        )
            else : 
                weather_data = {
                'error' : "Location Not Found"
                }
        
        
        
    context = {
        'weather_data' : weather_data,
        'forecast_data' : forecast_list
    }
    return render(request, 'weather/home.html' , context)