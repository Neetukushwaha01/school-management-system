from django.shortcuts import render

# Create your views here.
from requests import Response
from rest_framework import generics, status
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer


class SchoolCreateView( generics.CreateAPIView ):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentBulkCreateView( generics.CreateAPIView ):
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        students = request.data
        for student in students:
            student['school'] = kwargs['pk']
        serializer = self.get_serializer( data=students, many=True )
        serializer.is_valid( raise_exception=True )
        serializer.save()

        return Response( serializer.data, status=status.HTTP_201_CREATED )


class StudentListView( generics.ListAPIView ):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        grade = self.request.query_params.get( 'grade', None )
        if grade is not None:
            queryset = queryset.filter( grade=grade )
        return queryset


class StudentUpdateView( generics.UpdateAPIView ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolUpdateView( generics.UpdateAPIView ):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolListView( generics.ListAPIView ):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
