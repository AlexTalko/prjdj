from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import CategoryListView, CategoryDetailView, ProductDetailView, ContactsTemplateView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('', CategoryListView.as_view(), name='category_list'),
    path('catalog/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
