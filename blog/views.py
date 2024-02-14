from django.shortcuts import render
from django.views.generic import ListView
from .models import Lugat

class LugatListView(ListView):
    model = Lugat
    template_name = 'home.html'
    context_object_name = 'lugat_list'