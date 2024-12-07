from django.urls import path
from sample_api.views import *
urlpatterns=[
    path('',view_dtl,name='dtl'),
    path('view_student/',view_student,name='view_student'),
    path('students/<int:pk>/', view_student, name='view_student_detail'),

]