from django.shortcuts import render
from django.http import HttpResponse
from city.models import *


def CityView(request) -> render:
    city = City.objects.all()
    return render(request, "MainApp/cities.html", {"city": city})



