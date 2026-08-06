from django import forms
from myapp.models import Students

class StudentForm(forms.ModelForm):
    StuId=forms.IntegerField()
    StuName=forms.CharField(max_length=30)
    StuMarks=forms.IntegerField()
    StuImage=forms.CharField(max_length=1000)
    class Meta:
        model=Students
        fields='__all__'
