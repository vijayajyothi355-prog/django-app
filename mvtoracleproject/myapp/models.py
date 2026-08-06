from django.db import models

# Create your models here.
class Student(models.Model):
    StuID=models.IntegerField()
    StuName=models.CharField(max_length=30)
    StuMarks=models.IntegerField()
    StuImage=models.URLField(max_length=1000,blank=True,null=True)
    