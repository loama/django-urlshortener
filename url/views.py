from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import short_url

from url.models import shortened_url
# Create your views here.

from django.http import HttpResponse

def index(request, urlToShorten):
    return HttpResponse("Shortened " + urlToShorten)

def redirect(request, urlToRedirect):
    destination = shortened_url.objects.get(shortened_url='abc.co')
    return HttpResponseRedirect(str(destination))
