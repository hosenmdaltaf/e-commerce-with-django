
from django.urls import path
from forntpage import views


app_name ='forntpage'

urlpatterns = [
    path('',views.forntpage, name='home')
    # path('', ProductListView.as_view(), name='allproduct'),

]