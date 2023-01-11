from django.urls import path, include
from sandwiches.api import api_router
from wagtail.admin import urls as wagtailadmin_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', api_router.urls),
    path('wagtail-admin/', include(wagtailadmin_urls)),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
