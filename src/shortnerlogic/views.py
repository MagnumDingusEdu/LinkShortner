from django.shortcuts import render, redirect
from django.http.response import HttpResponse,  JsonResponse
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Link
from django.views.decorators.csrf import csrf_exempt
from ratelimit.decorators import ratelimit
# Create your views here.


@ratelimit(key='ip', rate='10/m', block=False)
def redirectHandler(request):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        messages.info(request, "You've made too many requests in a short time period. Please try again later.")
        return render(request, 'shortnerlogic/index.html', {}, status=403)
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
        else:
            messages.info(request, 'Invalid request')
            return render(request, 'shortnerlogic/index.html')
    elif Link.objects.filter(shorturl=pathargument).exists():
        thelinkobject = Link.objects.get(shorturl=pathargument)
        thelinkobject.clickcount += 1
        thelinkobject.save()
        return redirect(thelinkobject.longurl)


    else:
        messages.info(request, "This path was not found")
        return render(request, 'shortnerlogic/index.html')

@ratelimit(key='ip', rate='10/m', block=True)
@csrf_exempt
def generatorAPI(request):

    if request.method == "GET":
        return JsonResponse({"status_code":400, "shorturl":None,"message":"GET request not allowed on this endpoint. Read the docs at https://github.com/MagnumDingusEdu/LinkShortner"})
    elif request.method == "POST":
        longurl = request.POST.get('url',False)

        if longurl:
            validate = URLValidator()
            try:
                validate(longurl)
                generatedlink = Link.objects.create(
                    longurl = longurl
                )
                return JsonResponse({"status_code":200,"shorturl":"https://ln-k.cf/"+generatedlink.shorturl, "message":"Short URL Created Successfully !"})
            except ValidationError:
                return JsonResponse({"status_code":400,"shorturl":None, "message":"Invalid url"})
        else:
            return JsonResponse({"status_code":400,"shorturl":None, "message":"url parameter missing"})
        
    else:
        return JsonResponse({"status_code":400,"shorturl":None, "message":"Invalid request"})



def ratelimitedView(request, exception):
    return JsonResponse({"status_code":403, "shorturl":None, "message":"You have made too many requests in a short time period. Try again later."}, status=403)
