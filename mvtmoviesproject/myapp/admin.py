from django.contrib import admin
from myapp.models import Movies
# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display=['MovieName','MovieHero','MovieHeroine','MovieImage']
    model=Movies
admin.site.register(Movies,MoviesAdmin)    
