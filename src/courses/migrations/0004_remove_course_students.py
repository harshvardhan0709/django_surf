# Generated by Django 3.2.5 on 2021-07-28 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]
