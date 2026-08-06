from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='signup'),
    path('login/',views.login),
    path('about/',views.about),
    path('contact/',views.contact),
    path('employees/',views.getemployees,name='emps'),
    path('edit/<int:id>',views.edit,name='modify'),
    path('find/<int:id>',views.find,name='modify'),
    path('delete/<int:id>',views.delemployee),
    
]