from django.urls import path
from . import views

urlpatterns = [
#    path('', views.course_list),
   path('', views.studentList, name="api-studentList"),  
   path('student-create/', views.studentCreate, name="api-studentCreate"),
   path('student-detail/<str:pk>/', views.studentDetail, name="api-studentDetail"),  
   path('student-update/<str:pk>/', views.studentUpdate, name="api-studentUpdate"),
   path('student-delete/<str:pk>/', views.studentDelete, name="api-studentDelete"),
   path('<str:pk>/course/', views.studentCourse, name="api-studentCourse"),         
   path('<str:pk>/course/add/', views.studentCoursePost, name="api-studentCoursePost"),
   path('<str:pk>/course/<str:course_id>/', views.studentCourseDelete, name="api-studentCourseDelete"),
]
