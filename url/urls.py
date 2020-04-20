from django.urls import path

from . import views

urlpatterns = [
    path('shorten/<str:urlToShorten>', views.index, name='index'),
    path('<str:urlToRedirect>', views.redirect, name='redirect'),
]
