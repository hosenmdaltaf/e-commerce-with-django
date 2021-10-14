from django.urls import path
from .import views
from .views import(
      ProfileUpdateView,
      ProfileDeleteView,
      ProfileDetailView,
)

app_name='accounts'
 
urlpatterns =[
    path('signup/',views.signup,name='signup'),
    path("login/",views.login_view,name='login'),
    path("logout/",views.logout_view,name='logout'),
    # path("profiledetail/<int:pk>/",views.profiledetail,name='profiledetail'),
    path('<int:pk>/',ProfileDetailView.as_view(), name='my_profile'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path('delete/<int:pk>',  ProfileDeleteView.as_view(), name='profile_delete'),
  
]
