from .models import Employee
from .serializers import EmployeeSerializer 
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission

class EmployeeModelViewSet(viewsets.ModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	authentication_class=[SessionAuthentication]
	permission_classes=[MyPermission]