from django.db import models
from django.db.models.base import Model

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    information = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    