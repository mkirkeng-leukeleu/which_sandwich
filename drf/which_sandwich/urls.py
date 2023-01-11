from django.urls import path, include
from . import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('get-api-token/', obtain_auth_token, name='get_api_token'),

    path('api/', include('api.urls')),
    path('sandwiches/', include('sandwiches.urls'))
]
