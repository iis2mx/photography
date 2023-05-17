from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('baby', views.baby, name='baby'),
    path('country', views.country, name='country'),
    path('product', views.product, name='product')

]