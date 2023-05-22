#GenericAPiView and ModelMixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin ,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# from rest_framework import viewsets

class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    

class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
















'''//..... Function Based View....//'''
'''
from django.shortcuts import render

from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view 
@api_view(['GET','PUT','PATCH','POST', 'DELETE'])
def StuApi(request, pk=None):
    if request.method == 'GET':
       id=pk
       if id is not None:
           stu=Student.objects.get(id=id)
           serializer=StudentSerializer(stu)
           return Response(serializer.data)
       stu=Student.objects.all()
       serializer=StudentSerializer(stu,many=True)
       return Response(serializer.data)
    
    if request.method =='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Created Data'})
        return Response(serializer.error)
     

    if request.method == 'PUT':
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update'})
        return Response(serializer.error)
    

    if request.method == 'PATCH':
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update'})
        return Response(serializer.error)

    if request.method == 'DELETE':
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Message Delete'})
'''







'''................Class Based View...........'''
'''
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
class StudentAPI(APIView):
    def get(self,request,pk=None,default=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,default=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Success'})
        return Response({'msg':'SOmthing Wrong'})
    
    def put(self,request,pk=None,default=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update'})
        return Response(serializer.error)
    
    def patch(self,request,pk=None,default=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update'})
        return Response(serializer.error)
    
    def delete(self,request,pk=None,default=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Message Delete'})
'''




