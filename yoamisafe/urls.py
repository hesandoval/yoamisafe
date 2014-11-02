from yoamisafe import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^/map/', views.map, name='map'),
    url(r'/temp', views.temp, name='temp'),
)
