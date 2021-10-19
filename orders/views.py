from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import(
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import Profile
from products.models import Product

from orders.models import OrderItem, Order



# @login_required
# def cart(request, slug):
#     item = get_object_or_404(Product, slug=slug)
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
#     print('-------------------------------------')
#     print(order_item)
    # order_qs = Order.objects.filter(user=request.user, ordered=False)
    # if order_qs.exists():
    #     order = order_qs[0]
    #     # check if the order item is in the order
    #     if order.items.filter(item__slug=item.slug).exists():
    #         order_item.quantity += 1
    #         order_item.save()
    #         messages.info(request, "This item quantity was updated.")
    #         return redirect("orders:cart_summary")
    #     else:
    #         order.items.add(order_item)
    #         messages.info(request, "This item was added to your cart.")
    #         return redirect("orders:cart_summary")
    # else:
    #     ordered_date = timezone.now()
    #     order = Order.objects.create(
    #         user=request.user, ordered_date=ordered_date)
    #     order.items.add(order_item)
    #     messages.info(request, "This item was added to your cart.")
    #     return redirect("orders:cart_summary")



@login_required(login_url ='/accounts/login/')
def cart(request):
    # user=get_object_or_404(User, user=request.user)
    user=get_object_or_404(Profile, user=request.user)
    product_id= request.GET.get('product_id')
    product=Product.objects.get(id=product_id)
    # create orderItem of the selected product
    order_item,created = OrderItem.objects.get_or_create(item=product,user=request.user,ordered=False)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=product.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("orders:cart_summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("orders:cart_summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("orders:cart_summary") 
         # create order associated with the user
    # user_order,created= Order.objects.get_or_create(owner=user, is_ordered=False)
    # user_order.items.add(order_item)
    # for items in order_item:
    #     items.add(altaf)
    #     print(items)
    # Order.objects.create(user=user,ordered=False,items=order_item)
                        
    return redirect("orders:cart_summary")

    

def cart_summary(request):
    if request.user.is_authenticated:
        user=user=get_object_or_404(Profile, user=request.user)
        carts = Order.objects.filter(user=request.user,ordered=False)
        
        print('----------------------------------------------------')
        print('cart details',carts)
     
    return render(request, 'cart/cart.html', {'carts':carts})

# class OrderSummaryView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         try:
#             order = Order.objects.get(user=self.request.user, ordered=False)
#             context = {
#                 'object': order
#             }
#             return render(self.request, 'order_summary.html', context)
#         except ObjectDoesNotExist:
#             messages.warning(self.request, "You do not have an active order")
#             return redirect("/")


def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'orders/purchase_success.html', {})
