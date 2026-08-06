from django.db import models

# Create your models here.
class Student(models.Model):
    StuID=models.IntegerField()
    StuName=models.CharField(max_length=30)
    StuMarks=models.DecimalField(max_digits=10,decimal_places=2)