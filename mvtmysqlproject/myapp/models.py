from django.db import models

# Create your models here.
class Products(models.Model):
    PID=models.IntegerField()
    PName=models.CharField(max_length=30)
    PPrice=models.IntegerField()
    PImage=models.CharField(max_length=1000)