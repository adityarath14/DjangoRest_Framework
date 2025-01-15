from django.urls import path
from Myapp.views import *
urlpatterns=[
    path('', Home.as_view()),
]