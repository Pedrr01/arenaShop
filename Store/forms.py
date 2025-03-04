from django import forms
from Store.models import Products

class ProductsForm(forms.ModelForm):

    class Meta:                  
        model = Products   
        fields = "__all__"   
    

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 500:
            self.add_error('price', 'Preço Muito Alto')
        return price