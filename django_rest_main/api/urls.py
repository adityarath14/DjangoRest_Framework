from django.urls import path, include
from api.views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employees', EployeeViewset, basename='employee')
urlpatterns = [
    # path('students/',students),
    # path('students/',studentsView),
    # path('students/<int:pk>/', studentDetailView),
    # path('employees/', Employees.as_view()),
    # path('employees/<int:pk>/', EmployeeDetails.as_view()),
    path('', include(router.urls)),
    path('blogs/', BlogsView.as_view()),
    path('comments/', CommentsView.as_view()),
    path('blogs/<int:pk>/', BlogDetailView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]