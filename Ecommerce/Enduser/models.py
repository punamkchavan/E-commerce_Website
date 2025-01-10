from django.db import models
from superadmin.models import Product
# Create your models here.
  
class Cart(models.Model):
    session_id = models.CharField(max_length=255)  # To track carts for anonymous users
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart ({self.session_id}) - {self.product.name} x {self.quantity}"


class UserAccount(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return self.user.username
    
    
 