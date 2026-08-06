from django.shortcuts import render
from django.urls import reverse_lazy
from myapp.models import Product
from django.views.generic import *

class RegisterProduct(CreateView):
    model=Product
    fields='__all__'

class ProductList(ListView):
    model=Product
    fields='__all__'

class ModifyProduct(UpdateView):
    model=Product
    fields='__all__' 

class FindProduct(DetailView):
    model=Product
    fields='__all__'   

class RemoveProduct(DeleteView):
    model=Product
    success_url=reverse_lazy("products")     