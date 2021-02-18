from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "dense_find_app/index.html" #dense_find_app/templates/dense_find_app/index.html
    
    