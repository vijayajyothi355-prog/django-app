from django.shortcuts import render
from myapp.models import Doctor
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
class DoctorList(ListView):
    model=Doctor
    fields='__all__'
class RegisterDoctor(CreateView):
    model=Doctor
    fields='__all__'   
class ModifyDoctor(UpdateView):
    model=Doctor
    fields='__all__'     
class FindDoctor(DetailView):
    model=Doctor
    fields='__all__'   
class RemoveDoctor(DeleteView):
    model=Doctor
    success_url=reverse_lazy('doctors')     
