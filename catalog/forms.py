from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']