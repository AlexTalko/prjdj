from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        prohibit_words = ['казино', 'криптовалюта', 'крипта',
                          'биржа', 'дешево', 'бесплатно', 'обман',
                          'полиция', 'радар',]
        if cleaned_name in prohibit_words:
            raise forms.ValidationError('В названии присутствуют запрещенные слова')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        prohibit_words = ['казино', 'криптовалюта', 'крипта',
                          'биржа', 'дешево', 'бесплатно', 'обман',
                          'полиция', 'радар',]
        if cleaned_description in prohibit_words:
            raise forms.ValidationError('В описании присутствуют запрещенные слова')
        return cleaned_description


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
