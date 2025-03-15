from django.db import models

# Classe para o ADM cadastrar os esportes:

class SportCategoryFK(models.Model):
    sport = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.sport

# Classe para os usuários cadastrarem os produtos:

class Products(models.Model):
    product = models.CharField(max_length=255) 
    mark = models.CharField(max_length=255) 
    sport = models.ForeignKey(SportCategoryFK, on_delete=models.PROTECT, related_name="Product_Sport")
    description = models.TextField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    photo = models.ImageField(upload_to="products/", blank=True, null=True, default='default_product.png')
    status = models.CharField(max_length=50, choices=[('indisponível', 'indisponível'), ('disponível', 'disponível')], default='disponível')  
    contact = models.CharField(max_length=255)  
    
    def __str__(self):
        return f'{self.product} para - {self.sport}'