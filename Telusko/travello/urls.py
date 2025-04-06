from django.urls import path
from travello.views import *
urlpatterns = [
    path('', index, name='index'),
]