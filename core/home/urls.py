from django.contrib import admin
from django.urls import path,include
from home.views import *
urlpatterns=[
    path('',home),
    path('Student/',post_student)
]