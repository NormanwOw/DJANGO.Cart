from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart-update/', views.cart_update, name='cart-update'),
    path('cart-add/', views.cart_add, name='cart-add'),
    path('new-order/', views.new_order, name='new-order'),
    path('accept-order/', views.AcceptOrderView.as_view(), name='accept-order'),
]
