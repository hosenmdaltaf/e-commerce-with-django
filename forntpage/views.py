import products
from django.shortcuts import render
from products.models import Product,Category

def forntpage(request):
    products=Product.objects.all()
    categorys=Category.objects.all()

    context ={
        'products':products,
        'categorys':categorys
    }

    return render(request, 'forntpage/forntpage.html',context)
