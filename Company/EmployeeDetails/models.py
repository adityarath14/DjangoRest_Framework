from django.db import models

# Create your models here.
class Emp(models.Model):
    Empno=models.IntegerField()
    Empname=models.CharField(max_length=100)
    Roal=models.CharField(max_length=100)
    Email=models.EmailField()
    def __str__(self):
        return self.Empname