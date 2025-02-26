from django import forms
from Store.models import Products

class ProductsForm(forms.ModelForm):

    class Meta:                  
        model = Products   
        fields = "__all__"   
        widgets = {
        'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
        'mark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
        'sport': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Esporte'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
        'photo': forms.FileInput(attrs={'class': 'form-control'}),
        'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contato'}),
        }