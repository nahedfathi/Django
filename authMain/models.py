from django.db import models

# Create your models here.

class AuthMain(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.username
    