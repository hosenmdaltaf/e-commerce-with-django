from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    #feactured
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_img',default='/static/images/cover.jpg')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return reverse('shop:product_detail', args=[self.id, self.slug])

    # def get_add_to_cart_url(self):
    #     return reverse("products:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("products:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })


# class Variation(models.Model):
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)  

#     class Meta:
#         unique_together = (
#             ('item', 'name')
#         )

#     def __str__(self):
#         return self.name


# class ProductVariation(models.Model):
#     variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
#     value = models.CharField(max_length=50)  # S, M, L

#     attacment = models.ImageField(blank=True)

#     class Meta:
#         unique_together = (
#             ('variation', 'value')
#         )

#     def __str__(self):
#         return self.value
