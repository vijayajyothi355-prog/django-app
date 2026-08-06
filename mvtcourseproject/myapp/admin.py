from django.contrib import admin
from myapp.models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=['CourseID','CourseName','CoursePrice','CourseImage']
    model=Course
admin.site.register(Course,CourseAdmin)    