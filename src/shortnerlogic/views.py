from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Link
# Create your views here.



def redirectHandler(request):
    pathargument = request.path[1:]
    
    if pathargument == "":
        if request.method == "GET":
            return render(request, 'shortnerlogic/index.html', {})
        elif request.method  == "POST":
            longurl = request.POST.get('longurl',False)

            if longurl:
                validate = URLValidator()
                try:
                    validate(longurl)
                    generatedlink = Link.objects.create(
                        longurl = longurl
                    )
                    messages.info(request, f'Your shortned URL is')
                    return render(request, 'shortnerlogic/index.html', {'newlink':generatedlink.shorturl})
                except ValidationError:
                    messages.info(request, 'This URL is invalid.')
            return render(request, 'shortnerlogic/index.html', {'oldurl':longurl})
    elif Link.objects.filter(shorturl=pathargument).exists():
        thelinkobject = Link.objects.get(shorturl=pathargument)
        thelinkobject.clickcount += 1
        thelinkobject.save()
        return redirect(thelinkobject.longurl)
    else:
        messages.info(request, "This path was not found")
        return render(request, 'shortnerlogic/index.html')


