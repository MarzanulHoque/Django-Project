from django.shortcuts import render
from rest_framework import viewsets
from DjangoMedicalApp.models import Company
from DjangoMedicalApp.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(viewsets.ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        company = Company.objects.all()
        serializer = CompanySerializer(company,many=True,context={"request":request})
        response_dict = {"error":False,"message":"All Company List Data","Data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = CompanySerializer(data=request.data, context = {"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error":False,"message":"Company Data saved Successfully"}
        except:
            dict_response={"error":True,"message":"error During Saving company data"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset = Company.objects.all()
            company= get_object_or_404(queryset,pk=pk)
            serializer=CompanySerializer(company,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error":False,"message":"Successfully updated Company Data "}
        except:
            dict_response = {"error":True,"message":"Error During Updating Company Data "}
        
        return Response(dict_response)


 
company_list = CompanyViewSet.as_view({"get":"list"})
company_creat = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put" : "update"})
