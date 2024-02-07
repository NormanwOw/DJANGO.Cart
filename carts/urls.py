from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('new-order/', views.new_order, name='new-order'),
]
