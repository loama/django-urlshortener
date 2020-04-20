from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
import random
import string
import short_url

from url.models import shortened_url
# Create your views here.

from django.http import HttpResponse

def index(request, urlToShorten):
    # generate random code
    letters = string.ascii_letters
    id = ''.join(random.choice(letters) for i in range(3))

    url = shortened_url(original_url=urlToShorten, shortened_url=id)
    url.save()
    return JsonResponse({
        'status': 'success',
        'data': {
            'original_url': urlToShorten,
            'shorten_url': id
        }
    })

def redirect(request, urlToRedirect):
    print(urlToRedirect)
    destination = shortened_url.objects.get(shortened_url=urlToRedirect)
    return HttpResponseRedirect(str(destination))
