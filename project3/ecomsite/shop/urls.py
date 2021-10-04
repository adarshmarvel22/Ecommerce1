from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.index,name='shop'),
   path("checkout",views.checkout,name='checkout'),
   path("<int:id>/",views.detail,name='detail'),
]
