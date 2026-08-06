from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.home),
    path('students/',views.getstudents),
    path('products/',views.getproducts),
    path('customers/',views.getcustomers),
    

]