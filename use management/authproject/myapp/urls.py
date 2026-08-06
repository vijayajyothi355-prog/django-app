from django.urls import path,include
from myapp import views
urlpatterns=[
    path('',views.home),
    path('python/',views.pythonexam),
    path('ui/',views.uiexam),
    path('java/',views.javaexam),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',views.register),

]