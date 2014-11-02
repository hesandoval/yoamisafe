from django.shortcuts import render
from django.http import HttpResponse
from yoamisafe.models import Incident
import requests
YO_API = "http://api.justyo.co/yo/"
YO_API_TOKEN = "742a63e4-3aa2-4acd-a5dd-5540de7f415f"
# Create your views here.
def map(request):
    for res in request.GET:
        if(request.GET[res] == ""):
            longitude = res
            break
    latitude = request.GET['location']
    username = request.GET['username']

    r = requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN, 'username': username})

    return HttpResponse(r.text)


def displayMap(request, longitude, latitude, username):
    context = {}
    context['userLatitude'] = latitude
    context['userLongitude'] = longitude
    context['username'] = username
    #latitude range = .0045


    return HttpResponse("Hello from temp")