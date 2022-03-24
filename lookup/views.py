from django.shortcuts import render
#import requests
# Create your views here.
def home(request):
    
    import json
    import requests
    
    #call the API 
    api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=02151,us&type=accurate&units=imperial&temp_max=Fahrenheit&appid=472711ccd55e2e7b66a5a6554fcd2261")
    
    try:
        api = json.loads(api_request.content.decode('utf-8'))
    except Exception as e:
        api = "Error"
    
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})