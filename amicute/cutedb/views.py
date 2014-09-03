from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model

from django.views.generic.edit import CreateView

from .forms import UserCreationForm
# Create your views here.


class UnauthorizedHomePageView(TemplateView):

    template_name = "unauthorized_homepage.html"


class Register(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    model = get_user_model()
    success_url = '/'
