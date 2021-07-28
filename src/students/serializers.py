from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'courses':{'required': False}}

class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id','first_name','last_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')