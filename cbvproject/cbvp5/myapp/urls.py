from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.DoctorList.as_view(),name='doctors'),
    path('create/',views.RegisterDoctor.as_view()),
    path('edit/<int:pk>/',views.ModifyDoctor.as_view()),
    path('<int:pk>/',views.FindDoctor.as_view()),
    path('delete/<int:pk>/',views.RemoveDoctor.as_view()),
]