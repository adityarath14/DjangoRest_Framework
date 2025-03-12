from django.shortcuts import render
from employees.models import Employee
# Create your views here.
def EmployeeDetails(request):
    employee=Employee.objects.all()
    context={'employee':employee}
    return render(request, 'employee_details.html', context)
def ShowInformation(request, pk):
    employee=Employee.objects.get(pk=pk)
    context={'employee':employee}
    return render(request, 'show_information.html', context)