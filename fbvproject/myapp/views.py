from django.shortcuts import render,redirect
from myapp.forms import StudentForm
from myapp.models import Students
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def register(request):
    StuForm = StudentForm()
    if request.method == 'POST':
        StuForm = StudentForm(request.POST)
        if StuForm.is_valid():
            StuForm.save(commit=True)
            return redirect('/students')
    return render(request,'myapp/register.html',{'Form':StuForm})
    
def login(request):
    return render(request,'myapp/login.html')
def about(request):
    return render(request,'myapp/about.html')
def contact(request):
    return render(request,'myapp/contact.html')
def getstudents(request):
    student = Students.objects.all()
    return render(request,'myapp/students.html',{'stulist':student})

    