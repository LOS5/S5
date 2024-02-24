from django.shortcuts import render

# Do it #3
from django.views.generic import TemplateView,CreateView

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
