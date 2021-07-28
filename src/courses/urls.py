from django.urls import path
from . import views

urlpatterns = [
   path('', views.courseList, name="api-courseList"),  
   path('course-create/', views.courseCreate, name="api-courseCreate"),
   path('course-detail/<str:pk>/', views.courseDetail, name="api-courseDetail"),  
   path('course-update/<str:pk>/', views.courseUpdate, name="api-courseUpdate"),
   path('course-delete/<str:pk>/', views.courseDelete, name="api-courseDelete"),     
   path('<str:pk>/student/', views.courseStudentList, name="api-courseStudentList"),         
   path('<str:pk>/student/add/', views.courseStudentAdd, name="api-courseStudentAdd"),
   path('<str:pk>/student/<str:student_id>/', views.courseStudentDelete, name="api-courseStudentDelete"),
]
