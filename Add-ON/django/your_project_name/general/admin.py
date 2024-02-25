from django.contrib import admin

from general.models import FeedbackModel#3
from general.models import LoginModel#
# Register your models here.

admin.site.register(FeedbackModel)#7
admin.site.register(LoginModel)
