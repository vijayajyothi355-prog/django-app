from django.shortcuts import render
from myapp.models import Movies
# Create your views here.
def home(request):
    movie=Movies.objects.all()
    return render(request,'home.html',{'movielist':movie})