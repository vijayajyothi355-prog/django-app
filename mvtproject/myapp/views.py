from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def home(request):
    Students=Student.objects.all()
    return render(request,'myapp/home.html',{'Stulist':Students})