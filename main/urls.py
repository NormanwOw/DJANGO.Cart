from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.ProductsView.as_view(), name='products'),
]
