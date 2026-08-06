from django.shortcuts import render,redirect,get_object_or_404
from myapp.forms import EmployeeForm
from myapp.models import Employee

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    EmpForm = EmployeeForm()
    if request.method == 'POST':
        EmpForm = EmployeeForm(request.POST)
        if EmpForm.is_valid():
            EmpForm.save(commit=True)
            return redirect('/employees')
    return render(request,'register.html',{'Form':EmpForm})

def about(request):
    return render(request,'about.html')



def edit(request,id):
    Emply = Employee.objects.get(pk=id)
    EmplyForm = EmployeeForm(instance=Emply)
    if request.method=='POST':
        EmplyForm = EmployeeForm(request.POST,instance=Emply)
        EmplyForm.save()
        return redirect("/employees")
    return render(request,'edit.html',{'Form':EmplyForm})      
                  

def find(request,id):
    employee=get_object_or_404(Employee,EmpId=id)
    return render(request,'find.html',{'emp':employee})



def login(request):
    return render(request,'login.html')
def contact(request):
    return render(request,'contact.html')

def getemployees(request):
    Employees = Employee.objects.all()
    return render(request,'employees.html',{'EmpList':Employees})

def delemployee(request,id):
    emply=get_object_or_404(Employee,EmpId=id)
         
    if request.method=='POST':
        emply.delete()
        return redirect('/employees')
    return render(request,'delete.html')

