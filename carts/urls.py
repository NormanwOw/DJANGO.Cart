from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-add/', views.cart_add, name='cart-add'),
    path('new-order/', views.new_order, name='new-order'),
]
