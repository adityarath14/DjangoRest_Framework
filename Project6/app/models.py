from django.db import models

# Create your models here.
class Product_Cat(models.Model):
    pid=models.IntegerField(primary_key=True,default=None)
    pcat=models.CharField(max_length=100)
    def __str__(self):
        return self.pcat
class Product(models.Model):
    category=models.ForeignKey(Product_Cat,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_brand=models.CharField(max_length=100)