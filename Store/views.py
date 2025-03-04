from django.shortcuts import render
from django.views.generic import ListView, CreateView,  DetailView
from Store.models import Products
from Store.forms import ProductsForm

class ProductListView(ListView):
    model = Products
    template_name = 'list_products.html'
    context_object_name = 'product'       
                                                    
    def get_queryset(self):
        product = super().get_queryset().order_by('product')
        search = self.request.GET.get('search')
        if search:
            product = product.filter(product__icontains=search)
        return product

class ProductCreate(CreateView):
    model = Products
    form_class = ProductsForm
    template_name = 'create_products.html'
    success_url = '/list/'

class CarDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'