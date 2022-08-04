from django.shortcuts import render
from pip._vendor import requests
from django.http.response import JsonResponse
from django.http import HttpResponse

# Create your views here.
'''def home(request):
    url= 'https://api.openweathermap.org/data/2.5/weather?q=London&APPID=XXXXXXXXXXXXXXXXXXX'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data,safe=False)'''

# tying dynamic way 
def weatherByCity(request,city):
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=59d368eb73118e986bacb845e45dbec5'
    try:
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data,safe=False)
    except:
        return JsonResponse("error msg",safe=False)
#HOME PAGE 
def home(request):    
      return HttpResponse("welcome to My django application ")          
