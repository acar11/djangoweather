from django.shortcuts import render
#from sklearn.cross_validation import StratifiedShuffleSplit
#import requests
# Create your views here.
def home(request):
    
    import json
    import requests
    
    if request.method == "POST":
        #do post stuff
        zipcode = request.POST['zipcode']
        #return render(request, 'home.html', {'zipcode':zipcode}) 
                #call the API 
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + ",us&type=accurate&units=imperial&temp_max=Fahrenheit&appid=472711ccd55e2e7b66a5a6554fcd2261")
            
        try:
            api = json.loads(api_request.content.decode('utf-8'))
        except Exception as e:
            api = "Error"
            
        return render(request, 'home.html', {'api': api})
        
    else:

        #call the API 
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=02151,us&type=accurate&units=imperial&temp_max=Fahrenheit&appid=472711ccd55e2e7b66a5a6554fcd2261")
            
        try:
            api = json.loads(api_request.content.decode('utf-8'))
        except Exception as e:
            api = "Error"
            
        return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})