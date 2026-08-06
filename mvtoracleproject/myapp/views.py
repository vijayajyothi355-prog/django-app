from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def home(request):
    students=Student.objects.all()
    
    return render(request,'home.html',{'stulist':students})
