from django.contrib import admin
from Store.models import SportCategoryFK, Products

# Registrando Classe do BD

class SportCategoryFKAdmin(admin.ModelAdmin):
    list_display = ('sport', 'description')
    search_fields = ('sport',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'sport', 'description', 'price', 'photo', 'status', 'contact')
    search_fields = ('product', 'sport',)

admin.site.register(SportCategoryFK, SportCategoryFKAdmin)
admin.site.register(Products, ProductsAdmin)