from django.contrib import admin
from myapp.models import Products
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=['PID','PName','PPrice','PImage']
    model=Products
admin.site.register(Products,ProductsAdmin)
