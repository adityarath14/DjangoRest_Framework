from django.db import models

# Create your models here.
class Employee (models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='images/')
    degnination=models.CharField(max_length=100)
    email_address=models.EmailField(max_length=100, unique=True)
    def __str__(self):
        return self.first_name