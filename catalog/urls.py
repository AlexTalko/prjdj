from django.urls import path
from catalog.views import category_main_page, category_one, contacts, products, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', category_main_page, name='category_main_page'),
    path('catalog/<int:pk>/', category_one, name='category_one'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', product_detail, name='prod_info'),
]
