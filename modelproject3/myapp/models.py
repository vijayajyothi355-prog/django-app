from django.db import models


# Create your models here.
class Customer(models.Model):
    CusID=models.IntegerField()
    CusName=models.CharField(max_length=30)
    CusNo=models.DecimalField(max_digits=12,decimal_places=2)