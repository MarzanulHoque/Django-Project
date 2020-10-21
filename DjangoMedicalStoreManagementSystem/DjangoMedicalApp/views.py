from django.shortcuts import render
from rest_framework import viewsets
from DjangoMedicalApp.models import Company ,CompanyBank
from DjangoMedicalApp.serializers import CompanySerializer,CompanyBankSerializer
from rest_framework import generics
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
            serializer.is_valid(raise_exception=True)
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
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error":False,"message":"Successfully updated Company Data "}
        except:
            dict_response = {"error":True,"message":"Error During Updating Company Data "}
        
        return Response(dict_response)

class CompanyBankViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self,request):
        try:
            serializer =  CompanyBankSerializer(data=request.data, context = {"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error":False,"message":"Company Bank Data saved Successfully"}
        except:
            dict_response={"error":True,"message":"error During Saving company Bank data"}
        return Response(dict_response)

    def list(self,request):
        companybank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(companybank,many=True,context={"request":request})
        response_dict = {"error":False,"message":"All CompanyBank List Data","Data":serializer.data}
        return Response(response_dict)
    
    def retrieve(self,request,pk=None):
        queryset=CompanyBank.objects.all()
        companybank=get_object_or_404(queryset,pk=pk)  
        serializer = CompanyBankSerializer(companybank,context={"request":request})

        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})
    
    def update(self,request,pk=None):
        queryset=CompanyBank.objects.all()
        companybank=get_object_or_404(queryset,pk=pk)  
        serializer = CompanyBankSerializer(companybank,data=request.data,context={"request":request})

        serializer.is_valid()
        serializer.save()

        return Response({"error":False,"message":"Data has been updated  "})

class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        name=self.kwargs["name"]
        return Company.objects.filter(name=name)




    

company_list = CompanyViewSet.as_view({"get":"list"})
company_creat = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put" : "update"})
