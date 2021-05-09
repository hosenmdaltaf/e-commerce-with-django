from django.contrib import admin
# from .models import (
#     Product,Variation, ProductVariation,Category
# )


from .models import Category, Product


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name', )}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price',
#                     'available', 'created_at', 'created_at']
#     list_filter = ['available', 'created_at', 'created_at']
#     list_editable = ['price', 'available']
#     prepopulated_fields = {'slug': ('name', )}

# class ProductVariationAdmin(admin.ModelAdmin):
#     list_display = ['variation',
#                     'value',
#                     'attachment']
#     list_filter = ['variation', 'variation__item']
#     search_fields = ['value']


# class ProductVariationInLineAdmin(admin.TabularInline):
#     model = ProductVariation
#     extra = 1


# class VariationAdmin(admin.ModelAdmin):
#     list_display = ['item',
#                     'name']
#     list_filter = ['item']
#     search_fields = ['name']
#     inlines = [ProductVariationInLineAdmin]


# admin.site.register(ProductVariation, ProductVariationAdmin)
# admin.site.register(Variation, VariationAdmin)
admin.site.register(Product)
admin.site.register(Category)