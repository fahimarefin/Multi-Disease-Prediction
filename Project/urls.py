from django.contrib import admin
from django.urls import path, include
from project412 import views  # Make sure to import your views module
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project412.urls')),
   # path('', views.index, name='index'),  # Add this line for the root URL
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns +=path('__debug__/',include(debug_toolbar.urls)),