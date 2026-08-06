from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.ProductList.as_view(),name='products'),
    path('create/',views.RegisterProduct.as_view()),
    path('<int:pk>/',views.FindProduct.as_view()),
    path('edit/<int:pk>/',views.ModifyProduct.as_view()),
    path('delete/<int:pk>/',views.RemoveProduct.as_view()),
]