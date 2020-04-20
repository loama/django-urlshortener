from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request, urlToShorten):
    return HttpResponse("Shortened " + urlToShorten)

def redirect(request):
    return HttpResponse("Hello, you´ll be redirected")
