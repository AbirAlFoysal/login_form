from django.urls import path
from . import views
from django.urls import  include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name ="home"),
    path('login/', views.login, name ="login"),
    path('register/', views.registration, name ="registration"),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    
    path('login/',views.user_login,name='user_login'),
    
]

urlpatterns += staticfiles_urlpatterns()
