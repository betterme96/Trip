from django.conf.urls import url
from django.urls import path
from tripdiary import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]