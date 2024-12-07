from django.urls import path
from app.views import *
urlpatterns=[
    path('',view_dtl,name='view_dtl'),
    path('Person/',view_person,name='Person')
]