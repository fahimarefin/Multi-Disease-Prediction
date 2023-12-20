from django.contrib import admin
from django.urls import path, include
from project412 import views  
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project412.urls')),
   
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns +=path('__debug__/',include(debug_toolbar.urls)),