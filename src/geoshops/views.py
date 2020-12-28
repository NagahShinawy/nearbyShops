from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.utils.deprecation import DeprecationInstanceCheck
from django.views import generic
from .models import Shop


# default
latitude = 31.090745555630683
longitude = 31.621295675090344


user_location = Point(longitude, latitude, srid=4326)


def home(request):
    # shops = Shop.objects.annotate(
    #     distance=Distance("location", user_location)).order_by("distance")[0:6]
    shops = Shop.objects.all()[:6]
    return render(request, 'geoshops/home.html', {'shops': shops})


class HomeView(generic.ListView):
    model = Shop
    template_name = 'geoshops/index.html'
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)).order_by("distance")[0:6]
    context_object_name = 'shops'