from django.db import models

# Create your models here.
class Movies(models.Model):
    MovieName=models.CharField(max_length=30)
    Hero=models.CharField(max_length=20)
    Heroine=models.CharField(max_length=20)
    Budget=models.DecimalField(max_digits=12,decimal_places=2)