from django.shortcuts import render
from myapp.models import Movies
# Create your views here.
def home(request):
    Movie=Movies.objects.all()
    return render(request,'myapp/home.html',{'Movieslist':Movie})