from django.urls import path

from django.conf.urls import url

from flights  import views



urlpatterns = [

url(r'^search/', views.search, name="flightsearch"),
url(r'^datesearch/', views.datesearch, name="datesearch"),


]