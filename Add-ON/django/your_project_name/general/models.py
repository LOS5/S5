from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
        name=models.CharField(max_length=30)
        email=models.EmailField()
        contact=models.CharField(max_length=30)
        message=models.TextField(max_length=500)
        place=models.CharField(max_length=50,null=True,blank=True)

        def __str__(self):
            return self.name