from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from general.models import FeedbackModel, LoginModel
from general.forms import FeedbackForm, LoginForm


# Create your views here.

class CreateFeedbackView(CreateView):
    template_name= 'create_feedback.html'
    model= FeedbackModel
    form_class= FeedbackForm
    success_url = '/gen/home'

class CreateLoginView(CreateView):
    template_name= 'login.html'
    model= LoginModel
    form_class= LoginForm
    success_url = '/gen/home'

class HomePageView(TemplateView):
    template_name='index.html'
# Till here #10

class CreateRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class DemoPageView(TemplateView):
    template_name='demo.html'
# Till here #10

class RegisterPageView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
