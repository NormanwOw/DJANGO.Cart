from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('', include('carts.urls', namespace='carts')),
    path('users/', include('users.urls', namespace='users')),
]
