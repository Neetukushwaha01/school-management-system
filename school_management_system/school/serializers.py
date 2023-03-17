from rest_framework import serializers
from .models import School, Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'email', 'city', 'pin_code', 'password']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'username', 'password', 'grade', 'school']
