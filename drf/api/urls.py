from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('orders/', views.OrderList.as_view(), name='orders'),
]
