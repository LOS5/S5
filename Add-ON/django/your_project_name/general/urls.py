# create this file in general manually

# Do it 

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomePageView, CreateFeedbackView, RegisterView

from general.views import HomePageView,CreateFeedbackView

urlpatterns = [
    path('home/', HomePageView.as_view(),name='index_page'),
    path('feedback/', CreateFeedbackView.as_view(),name='feedback_page'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # Till here