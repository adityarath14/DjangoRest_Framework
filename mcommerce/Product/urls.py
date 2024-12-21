from django.urls import path
from Product.views import *
urlpatterns = [
    path('ListProduct/',ListProduct,name='ListProduct'),
    path('ListMessage/',ListMessage,name='ListMessage'), 
]