from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
import api.views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.conf import settings
from django.conf.urls.static import static
from sandwiches.api import api_router

urlpatterns = [
    # auth and admin
    path('admin/', admin.site.urls),
    path('get-api-token/', obtain_auth_token, name='get_api_token'),
    
    # api
    path('', api.views.IndexView.as_view(), name='index'),
    path('hello/', api.views.HelloView.as_view(), name='hello'),
    path('orders/', api.views.OrderList.as_view(), name='orders'),

    # wagtail
    path('sandwiches/', api_router.urls),
    path('wagtail-admin/', include(wagtailadmin_urls)),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
