from django.contrib import admin
from django.urls import path,include
from basicapp import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('basicapp.urls')),
    
]