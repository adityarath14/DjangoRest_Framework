from django.urls import path
from ToDo.views import *
urlpatterns = [
    path('', Home, name='Home'),
    path('AddTask/', AddTask, name='AddTask'),
    path('MarkAsDone/<int:pk>', MarkAsDone, name='MarkAsDone'),
    path('MarkAsUndone/<int:pk>/', MarkAsUndone, name='MarkAsUndone'),
    path('EditTask/<int:pk>/', EditTask, name='EditTask'),
    path('DeleteTask/<int:pk>/', DeleteTask, name='DeleteTask'),
]