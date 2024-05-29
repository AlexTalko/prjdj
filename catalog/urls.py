from django.urls import path
from catalog.views import home, contacts
from catalog.apps import CatalogConfig

new_app = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
