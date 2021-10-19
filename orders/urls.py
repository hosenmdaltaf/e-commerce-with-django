from django.urls import path
from orders import views
from .views import (
    cart,
    # cart_summary,
    # order_details,
    # checkout,

    success
)
from orders.views import(
OrderSummaryView

)

app_name ='orders'

urlpatterns = [
    # path('add_to_cart/<slug>/',views.add_to_cart,name="add_to_cart"),
    path('cart/',views.cart, name='cart'),
    # path('cart_summary/',views.cart_summary, name="cart_summary"),
    path('order-summary/', OrderSummaryView.as_view(), name='cart_summary'),
    # path('order_details/<int:pk>', OrderDetailsView.as_view(), name='order_summary'),
    path('success/',views.success, name='purchase_success'),
    # path('delete/<int:pk>/',views.delete_from_cart, name='delete_item'),

    # url(r'^checkout/$', checkout, name='checkout'),
   
]