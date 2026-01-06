from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.sample, name='sample'),
    path('my-name/', views.my_name, name='my_name'),
    path('order-list/', views.order_list, name='order_list'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('create-profile/', views.create_profile, name='create_profile'),
]