# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Image

# Create your views here.
class HomePageView(ListView):
    model = Image
    template_name = 'home.html'
    context_object_name = 'all_images_list'
    
class ProfilePageView(ListView):
    template_name = 'profile.html'