from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return render(request,'myapp/about.html')
def login(request):
    return render(request,'myapp/login.html')
def register(request):
    return render(request,'myapp/register.html')
def contact(request):
    return render(request,'myapp/contact.html')
