from django.db import models

# Create your models here.
class Admin(models.Model):
    username=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    c_password=models.CharField(max_length=200)
    
    def __str__(self):
        return self.username