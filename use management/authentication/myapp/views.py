from django.shortcuts import render,redirect
from myapp.forms import RegistrationForm
from django.contrib.auth.decorators import *
# Create your views here.
from django.contrib.auth.models import User
def home(request):
    return render(request,'myapp/home.html')
@login_required
def Javaexam(request):
    return render(request,'myapp/javaexam.html')
@login_required
def pythonexam(request):
    return render(request,'myapp/pythonexam.html')
@login_required
def uiexam(request):
    return render(request,'myapp/uiexam.html')
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return render(request,'myapp/home.html')
def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            return redirect('login')

    return render(request, 'myapp/register.html', {'form': form})
