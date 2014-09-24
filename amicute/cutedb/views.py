from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView

from braces.views import LoginRequiredMixin
from .forms import UserCreationForm
from .forms import CreatePostForm
from .models import Post
# Create your views here.


class UnauthorizedHomePageView(TemplateView):

    template_name = "unauthorized_homepage.html"


class Register(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    model = get_user_model()
    success_url = '/'


class AuthorizedHomePageView(LoginRequiredMixin, TemplateView):

    template_name = "authorized_homepage.html"

    def get_context_data(self, **kwargs):
        context = super(AuthorizedHomePageView, self).get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


class CreatePost(LoginRequiredMixin, CreateView):
    template_name = "create_post.html"
    model = Post
    form_class = CreatePostForm
    fields = ['image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreatePost, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
