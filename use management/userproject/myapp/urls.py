from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.Userlist.as_view(),name='users'),
     path('create/',views.CreateUser.as_view()),
      path('<int:pk>/',views.FindUser.as_view()),
      path('edit/<int:pk>/',views.UpdateUser.as_view()),
      path('delete/<int:pk>/',views.DeleteUser.as_view()),

]