from django.contrib import admin
from django.urls import path
from project412 import views
app_name = 'project412'
urlpatterns = [
  
 path("",views.index, name="index"),
 path('predict_image/', views.predict_image, name='predict_image'),
 path('signup/',views.signup,name='signup'),
 path('login/',views.log_in,name='login'),
 path('user_profile/', views.user_profile, name='user_profile'),
 path('predict_diabetes/', views.diabetes_prediction, name='diabetes_prediction')



]
