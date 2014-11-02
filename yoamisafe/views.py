from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def map(request):
    for res in request.GET:
        if(request.GET[res] == ""):
            #print "shit is empty yo"
            print res
            continue
        print request.GET[res]

    return HttpResponse(request.GET)

def temp(request):
    return HttpResponse("Hello from temp")