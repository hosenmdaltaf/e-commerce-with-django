from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import(
    DetailView
)

from accounts.models import Profile
from products.models import Product

from orders.models import OrderItem, Order


# def get_user_pending_order(request):
#     # get order for the correct user
#     user_profile = get_object_or_404(Profile, user=request.user)
#     order = Order.objects.filter(owner=user_profile, is_ordered=False)
#     if order.exists():
#         # get the only order in the list of filtered orders
#         return order[0]
#     return 0


def cart(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'cart/cart.html', {})



@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    # if product in request.user.profile.ebooks.all():
    #     messages.info(request, 'You already own this ebook')
    #     return redirect(reverse('products:product-list')) 
    # create orderItem of the selected product
    order_item = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order= Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    user_order.save()
    # if status:
    #     # generate a reference code
    #     user_order.ref_code = generate_order_id()
    #     user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('products:products.html'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('orders:order_summary'))



class OrderDetailsView(DetailView):
    model = OrderItem
    context_object_name = 'order_details'
    template_name ='orders/ordersdetails.html'

# @login_required()
# def order_details(request, **kwargs):
#     existing_order = get_user_pending_order(request)
#     context = {
#         'order': existing_order
#     }
#     return render(request, 'orders/order_summary.html', context)


def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'orders/purchase_success.html', {})
