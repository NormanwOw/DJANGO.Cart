from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.AuthLoginView.as_view(), name='login'),
]
