from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(20)
    description = models.CharField(100)
    price = models.DecimalField(10, 2)