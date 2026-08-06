from django.db import models

# Create your models here.
class Course(models.Model):
    CourseID=models.IntegerField()
    CourseName=models.CharField(max_length=30)
    CoursePrice=models.IntegerField()
    CourseImage=models.URLField(max_length=1000,blank=True,null=True)