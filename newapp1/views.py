from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employees
from .serializers import EmployeeSerializer

class EmployeesView(APIView):
    def get(self, request,e_id=None ):
        if e_id is not None:
            try:
                queryset = Employees.objects.get(id=e_id)  # Get queryset of YourModel instances
                serializer = EmployeeSerializer(queryset)
                return Response(serializer.data)
            except:
                return Response('Employee Not Found')
        else :
            queryset = Employees.objects.all()
            serializer = EmployeeSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Record id added')
        return Response('Provide valid data')

    def put(self,request,e_id):

        try:
            queryset = Employees.objects.get(id=e_id)  # Get queryset of YourModel instances
            serializer = EmployeeSerializer(queryset,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('Record id Updated')
            return Response('Provide valid data')
        except:
            return Response('Employee Not Found')




