from django.urls import path
from .views import *
urlpatterns=[
    path('',view_dtl,name='dtl'),
    path('Emp/',view_Emp,name='Emp'),
]