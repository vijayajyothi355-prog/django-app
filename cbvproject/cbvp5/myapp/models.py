from django.db import models
from django.urls import reverse
# Create your models here.
class Doctor(models.Model):
    DocterID=models.IntegerField()
    DoctorName=models.CharField(max_length=30)
    DoctorDesc=models.CharField(max_length=30)
    
    def get_absolute_url(self):
        return reverse('doctors')