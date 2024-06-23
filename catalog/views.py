from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_detail')


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'price', )
    success_url = reverse_lazy('catalog:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')
