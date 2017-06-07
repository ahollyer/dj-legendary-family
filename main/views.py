from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse

def home_redirect(request):
    return redirect(reverse('main:home'))

def home(request):
    return TemplateResponse(request, 'main/home.html', {})
