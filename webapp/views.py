from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import employees
from . serializer import employeeSerializer
# Create your views here.


class employeelist(APIView):
    def get(self,request):
        employee1=employees.objects.all()
        serializer=employeeSerializer(employee1,many=True)
        return Response(serializer.data)


    def post(self):
        pass