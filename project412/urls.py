from django.contrib import admin
from django.urls import path
from project412 import views

urlpatterns = [
  
 path("",views.index, name="index"),
 path('predict_image/', views.predict_image, name='predict_image'),
 path('signup/',views.signup,name='signup'),
 path('login/',views.log_in,name='login'),
 path('user_profile/', views.user_profile, name='user_profile'),



]
