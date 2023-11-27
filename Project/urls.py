from django.contrib import admin
from django.urls import path, include
from project412 import views  # Make sure to import your views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project412.urls')),
   # path('', views.index, name='index'),  # Add this line for the root URL
]