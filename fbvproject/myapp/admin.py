from django.contrib import admin
from myapp.models import Students
# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display=['StuId','StuName','StuMarks','StuImage']
    model=Students
admin.site.register(Students,StudentsAdmin)    
