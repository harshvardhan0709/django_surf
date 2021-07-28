from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets, status
from django.contrib.auth.models import User
from rest_framework import generics
from courses.serializers import StudentCourseSerializer
from .serializers import StudentSerializer,UserSerializer,RegisterSerializer
from .models import Student

# Create your views here.
@api_view(['GET'])
def studentList(request):
    student_list = Student.objects.all()
    serializer = StudentSerializer(student_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentDetail(request,pk):
    student = Student.objects.get(student_id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "Created Successfully"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def studentUpdate(request,pk):  
    student = Student.objects.get(student_id=pk)
    serializer = StudentSerializer(instance=student ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    if request.method ==  "GET":
        serializer1 = StudentSerializer(student, many=False)
        return Response(serializer1.data)
    return Response(serializer.data)

@api_view(['DELETE'])
def studentDelete(request,pk):  
    student = Student.objects.get(student_id=pk)
    student.delete()
    return Response('Item Succesfully delete!')

@api_view(['GET'])
def studentCourse(request,pk):  
    student = Student.objects.get(student_id=pk)
    courses = student.courses
    serializer = StudentCourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def studentCoursePost(request,pk):  
    student = Student.objects.get(student_id=pk)
    courses = student.courses.add(request.data["course"])
    student.save()
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def studentCourseDelete(request,pk,course_id):  
    student = Student.objects.get(student_id=pk)
    courses = student.courses.remove(course_id)
    student.save()
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@permission_classes((AllowAny,))
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })