from django.db import models

# Create your models here.
class Movies(models.Model):
    MovieName=models.CharField(max_length=30)
    MovieHero=models.CharField(max_length=30)
    MovieHeroine=models.CharField(max_length=30)
    MovieImage=models.URLField(max_length=1000, blank=True, null=True)