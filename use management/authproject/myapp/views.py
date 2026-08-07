from django.shortcuts import render,redirect
from django.contrib.auth.decorators import*
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
@login_required
def javaexam(request):
    return render(request,'myapp/javaexam.html')
@login_required
def pythonexam(request):
    return render(request,'myapp/pythonexam.html')

def uiexam(request):
    return render(request,'myapp/uiexam.html')
from django.http import HttpResponse
from myapp.forms import SignUpForm
def register(request):
    form = SignUpForm()
    if request.method=="POST":
        form =SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect('login')

    return render(request,'myapp/register.html',{'form':form})
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return render(request,'myapp/logout.html')