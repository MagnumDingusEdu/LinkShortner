from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Link
# Create your views here.


def notFound404View(request):
    return HttpResponse(request.path)



def redirectHandler(request):
    pathargument = request.path[1:]
    
    if pathargument == "":
        return HttpResponse('Welcome to ln-k URL Shortning service !')
    elif Link.objects.filter(shorturl=pathargument).exists():
        thelinkobject = Link.objects.get(shorturl=pathargument)
        return HttpResponse(thelinkobject.longurl)
    else:
        return HttpResponse("The path was not found")
