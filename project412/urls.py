from django.contrib import admin
from django.urls import path
from project412 import views

urlpatterns = [
  
    path("", views.predict_image, name='predict_image'),
    #path("",views.index, name="index")
    # Add other paths as needed for your app
]
