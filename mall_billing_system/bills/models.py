from django.db import models
from customers.models import Customer
from products.models import Product

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bill for {self.customer} on {self.date}'


# Create your models here.
