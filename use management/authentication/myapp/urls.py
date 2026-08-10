from django.urls import path,include
from myapp import views
urlpatterns=[
    path('',views.home),
    path('create/',views.register),
    path('javaexam/',views.Javaexam),
    path('pythonexam/',views.pythonexam),
    path('uiexam/',views.uiexam),
    path('accounts/',include('django.contrib.auth.urls'),name="login"),
    path('logout/',views.logout_view),

]