from django import forms
from general.models import FeedbackModel
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['name','email','contact','message','place']