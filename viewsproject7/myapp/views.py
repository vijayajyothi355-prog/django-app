from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    dict={"ID":111,"Name":"Kiran Kumar","Marks":4000 ,"Qualification":"Graduation","Age":20}
    return render(request,'myapp/home.html',dict)
