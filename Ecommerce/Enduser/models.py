from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shopee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=250)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
class First(models.Model):
    username=models.CharField(max_length=250)
    password1=models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.username
    

