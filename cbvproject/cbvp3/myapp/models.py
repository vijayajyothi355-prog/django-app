from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    ProID=models.IntegerField()
    ProName=models.CharField(max_length=30)
    ProPrice=models.IntegerField()
    def get_absolute_url(self):
       return reverse("products")