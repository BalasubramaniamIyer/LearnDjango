from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(20)
    description = models.TextField(100)
    price = models.DecimalField(10, 2)