from django.db.models import manager
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CourseSerializer
from students.serializers import CourseStudentSerializer
from .models import Course


@api_view(['GET'])
def courseList(request):
    course_list = Course.objects.all()
    serializer = CourseSerializer(course_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def courseDetail(request,pk):
    data={}
    try:
        course = Course.objects.get(name=pk)
        serializer = CourseSerializer(course, many=False)
        return Response(serializer.data)
    except:
        data["query_error"] = "Please check url"
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def courseCreate(request):
    data = {}
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data["success"] = "Created Successfully"
        return Response(data=data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def courseUpdate(request,pk):
    data={}
    try:
        course = Course.objects.get(name=pk)
        serializer = CourseSerializer(instance=course ,data=request.data)
        if serializer.is_valid():
            serializer.save()
        if request.method ==  "GET":
            serializer1 = CourseSerializer(course, many=False)
            return Response(serializer1.data)
        return Response(serializer.data)
    except:
        data["query_error"] = "Please check url"
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def courseDelete(request,pk):
    data = {}
    try:
        course = Course.objects.get(name=pk)
        course.delete()
        return Response('Item Succesfully delete!')
    except:
        data["query_error"] = "Please check url"
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def courseStudentList(request,pk):
    data = {}  
    try:
        course = Course.objects.get(name=pk)
        print(course)
        students = course.students
        print(students)
        serializer = CourseStudentSerializer(students, many=True)
        return Response(serializer.data)
    except:
        data["query_error"] = "Please check url"
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def courseStudentAdd(request,pk):  
    course = Course.objects.get(name=pk)
    student = course.students.add(request.data["student"])
    course.save()
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def courseStudentDelete(request,pk,student_id):  
    course = Course.objects.get(name=pk)
    student = course.students.remove(student_id)
    course.save()
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)
