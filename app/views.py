from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer


def index_page(request):
    employee = Employee.objects.get(position='ген.директор')
    context = EmployeeSerializer(employee).data
    return render(request, 'index.html', context)

