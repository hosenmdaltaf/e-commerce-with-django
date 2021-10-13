
from django.urls import path
from products import views
from products.views import(
   ProductDetailsView,CreateProductView,UpdateProductView,DeleteProductView

)
#  ProductListView,

app_name ='products'

urlpatterns = [
    path('products/',views.home,name='allproduct'),
    # path('products/', ProductListView.as_view(), name='allproduct'),
    path('details/<int:pk>', ProductDetailsView.as_view(), name='productdetails'),
    path('create/', CreateProductView.as_view(), name='Create_product'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete_product'),

    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profile/favourites/', views.favourite_list, name='favourite_list'),
]
