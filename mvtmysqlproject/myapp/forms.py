from django import forms
from myapp.models import Products
class ProductsForm(forms.ModelForm):
    PID=forms.IntegerField()
    PName=forms.CharField(max_length=30)
    PPrice=forms.IntegerField()
    PImage=forms.CharField(max_length=1000)
    class Meta:
        model = Products
        fields = '__all__'