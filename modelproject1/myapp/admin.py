from django.contrib import admin
from myapp.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    class meta:
        model=Product
admin.site.register(Product,ProductAdmin)        
