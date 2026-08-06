from django.shortcuts import render,redirect
from myapp.models import Products
from myapp.forms import ProductsForm
# Create your views here.
def home(request):
    Product=Products.objects.all()
    return render(request,'home.html',{"productslist":Product})
def register(request):
      Pform=ProductsForm()
      if request.method=='POST':
              Pform=ProductsForm(request.POST)
              if Pform.is_valid():
                      Pform.save(commit=True)
                      redirect('/')
      return render(request,'register.html',{'form':Pform})        
    