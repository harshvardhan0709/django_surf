from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #full_name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course, related_name='students',blank=True)

    class Meta:
        unique_together = ['first_name', 'last_name']
        ordering = ['first_name']

    def __str__(self):
        return self.full_name