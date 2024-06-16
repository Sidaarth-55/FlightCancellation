from django.db import models

# Create your models here.
class PDF(models.Model):
    name=models.CharField(max_length=32,unique=True)
    file=models.FileField()
    question=models.CharField(max_length=50)