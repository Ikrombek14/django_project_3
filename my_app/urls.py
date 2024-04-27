from django.urls import path
from .views import *

urlpatterns = [
    path('',object, name ='object_list'),
    path('product/', product, name = 'product')
]
