from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Category, Product


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_success_url(self):
        return reverse('catalog:category_detail', args=[self.kwargs.get('pk')])


class ProductDetailView(DetailView):
    model = Product
