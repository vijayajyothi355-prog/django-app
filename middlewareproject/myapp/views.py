from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    return HttpResponse(f"<h style='text-align:center; color:brown'>Division is : {5//2}</h1>")