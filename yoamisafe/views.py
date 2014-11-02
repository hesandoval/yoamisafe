from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def map(request, username, longitude, latitude):
    print "Username: ", username
    print "longitude: ", longitude
    print "latitude: ", latitude

def temp(request):
    return HttpResponse("Hello from temp")