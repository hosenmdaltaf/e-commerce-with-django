from django.db import models

from django.db import models
from accounts.models import Profile
from django.utils import timezone
from django.contrib.auth.models import User

from products.models import Product

#   user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"

#     def get_total_item_price(self):
#         return self.quantity * self.item.price
class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # item = models.OneToOneField(Product,on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    # date_added = models.DateTimeField(auto_now=True)
    # ordered_date = models.DateTimeField(null=True)
   

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_final_price(self):
        # if self.item.discount_price:
        #     return self.get_total_discount_item_price()
        return self.get_total_item_price()



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    # ordered_date = models.DateTimeField(null=True)
    # is_ordered=models.BooleanField(default=False)
    items=models.ManyToManyField(OrderItem)
    # items=models.ForeignKey(OrderItem, on_delete=models.SET_NULL,null=True)
    # product = models.OneToOneField(Product,on_delete=models.SET_NULL,null=True)
    # quantity = models.PositiveIntegerField(default=1)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
    
    def __str__(self):
        return str(self.user.username)
    


    

