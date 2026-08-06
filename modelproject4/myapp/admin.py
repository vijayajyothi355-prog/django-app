from django.contrib import admin
from myapp.models import Movies
# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    class meta:
        model=Movies
admin.site.register(Movies,MoviesAdmin)        