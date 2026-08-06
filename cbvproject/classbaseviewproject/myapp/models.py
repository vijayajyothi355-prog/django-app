from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    StuID=models.IntegerField(primary_key=True)
    StuName=models.CharField(max_length=30)
    StuMarks=models.IntegerField()
    def get_absolute_url(self):
        return reverse("students")