from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ConsumeAPP import views

urlpatterns = [
    #path('', views.home,name='home'),
    #url(r'^weather/<str:city>$',views.home),    #(?P<question_id>\d+)
    path('weather/<str:city>/', views.weatherByCity),
    path('home', views.home) ,   
]
