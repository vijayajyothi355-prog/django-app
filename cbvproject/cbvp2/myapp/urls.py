from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.ProductList.as_view(),name='products'),
    path('create/',views.CreateProduct.as_view()),
    path('<int:pk>/',views.ProductDetails.as_view()),
    path('edit/<int:pk>/',views.UpdateProduct.as_view()),
    path('delete/<int:pk>/',views.DeleteProduct.as_view()),
]