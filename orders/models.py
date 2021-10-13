from django.db import models

from django.db import models
from accounts.models import Profile
from datetime import datetime

from products.models import Product



class OrderItem(models.Model):
    product = models.OneToOneField(Product,on_delete=models.SET_NULL,null=True)
    # quantity = models.IntegerField(default=0)
    is_ordered=models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.title


class Order(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    ordered_date = models.DateTimeField(auto_now=True)
    is_ordered=models.BooleanField(default=False)
    items=models.ManyToManyField(OrderItem)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
    
    def __str__(self):
        return self.owner
    

