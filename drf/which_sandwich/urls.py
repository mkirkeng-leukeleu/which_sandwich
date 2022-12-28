from django.contrib import admin
from django.urls import path
from core import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-api-token/', obtain_auth_token, name='get_api_token'),
    
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('orders/', views.OrderList.as_view(), name='orders')
]
