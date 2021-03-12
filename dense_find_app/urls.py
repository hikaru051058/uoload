from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomeView.as_view(), name='index'),
    path('ebisu/',views.TokyoView.as_view()),
    path('nagoya/',views.NagoyaView.as_view()),
    path('shibuya/',views.ShibuyaView.as_view()),
    ]