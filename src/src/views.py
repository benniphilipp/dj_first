from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "home.html"

def home(request):
    return HttpResponse("<h1>Hallo Welt</h1>")
