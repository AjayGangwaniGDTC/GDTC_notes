import requests 

def get_weather(city):
    response=requests.get(f"htts://api.weather.com/{city}")
    print(response)
    # return response
    
get_weather(city="Mumbai")