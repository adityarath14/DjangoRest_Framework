from django.urls import path
from employees.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', EmployeeDetails, name='home'),
    path('showinformation/<int:pk>/',ShowInformation, name='employee_information'),
]
# Serve media files only during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
