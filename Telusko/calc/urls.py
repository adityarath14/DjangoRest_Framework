from django.urls import path
from calc.views import *
urlpatterns = [
    path('', Home, name='Home'),
    path('Add/', Add, name='Add'),
]