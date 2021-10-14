from django.urls import path
from orders import views


from .views import (
    add_to_cart,
    delete_from_cart,
    # order_details,
    # checkout,

    success
)
from orders.views import(
OrderDetailsView

)

app_name ='orders'

urlpatterns = [
    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('cart/',views.cart, name='cart'),
    # path('add_to_cart/<int:pk>/',views.order_details, name="order_summary"),
    path('order_details/<int:pk>', OrderDetailsView.as_view(), name='order_summary'),
    path('success/',views.success, name='purchase_success'),
    path('delete/<int:pk>/',views.delete_from_cart, name='delete_item'),

    # url(r'^checkout/$', checkout, name='checkout'),
   
]