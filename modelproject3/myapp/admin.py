from django.contrib import admin

from myapp.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    class meta:
        model=Customer
admin.site.register(Customer,CustomerAdmin)        

