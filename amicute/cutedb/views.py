from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model


from django.views.generic.edit import CreateView
# Create your views here.


class UnauthorizedHomePageView(TemplateView):

    template_name = "unauthorized_homepage.html"


class Register(CreateView):
    model = get_user_model()
    template_name = 'register.html'
    fields = ['username', 'password', 'email', 'birth_day']
    success_url = '/'
