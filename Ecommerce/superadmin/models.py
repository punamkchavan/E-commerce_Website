from django.db import models

# Create your models here.

class Host(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128) 
    ROLE_CHOICES = (
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        db_table = 'Host_Details'