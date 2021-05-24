
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.urls import path
from products import views
from products.views import(
    ProductListView,ProductDetailsView,CreateProductView,UpdateProductView,DeleteProductView

)

app_name ='products'

urlpatterns = [
    # path('products/',views.home, name='home')
    path('products/', ProductListView.as_view(), name='allproduct'),
    path('details/<int:pk>', ProductDetailsView.as_view(), name='productdetails'),
    path('create/', CreateProductView.as_view(), name='Create_product'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete_product'),

    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profile/favourites/', views.favourite_list, name='favourite_list'),
]
