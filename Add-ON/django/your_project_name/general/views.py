from django.shortcuts import render
from django.contrib.auth import login


# Do it #3
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from general.models import FeedbackModel
from general.forms import FeedbackForm



# Create your views here.

class CreateFeedbackView(CreateView):
    template_name= 'create_feedback.html'
    model= FeedbackModel
    form_class= FeedbackForm
    success_url = '/gen/home'

class HomePageView(TemplateView):
    template_name='index.html'
# Till here #10

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Automatically log in the user after successful registration
        login(self.request, self.object)
        return response
