from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import home, contacts
from catalog.apps import CatalogConfig

new_app = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
