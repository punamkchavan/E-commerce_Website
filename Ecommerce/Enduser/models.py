from django.db import models
 
# Create your models here.
  
class First(models.Model):
    username=models.CharField(max_length=250)
    password1=models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.username
    

