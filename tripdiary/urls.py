from django.conf.urls import url
from django.template.context_processors import static
from django.urls import path

from Trip import settings
from tripdiary import views
urlpatterns = [
    #path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('upload', views.upload, name='upload'),
    path('savediary', views.diary_save, name='savediary'),
    path('updatediary', views.diary_update, name='updatediary'),
    path('deletediary', views.diary_delete, name='deletediary'),
    path('userdiary', views.userdiary, name='userdiary'),
    path('alldiary', views.alldiary, name='alldiary'),
]