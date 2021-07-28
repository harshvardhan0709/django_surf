from rest_framework import serializers
from .models import Course
from students.serializers import StudentSerializer

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {'students':{'required': False}}

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id','name','information']