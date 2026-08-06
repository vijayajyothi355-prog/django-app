from django.db import models

# Create your models here.
class Product(models.Model):
    ProID=models.IntegerField()
    ProName=models.CharField(max_length=30)
    ProPrice=models.DecimalField(max_digits=8,decimal_places=2)