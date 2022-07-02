from django.contrib import admin
from django.urls import path
from .views import index, index2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
