from django.shortcuts import render
from django.views.generic import ListView
from Store.models import Products

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