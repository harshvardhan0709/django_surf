from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.test.client import Client
from courses.models import Course

class CoursesTests(APITestCase):
    def setUp(self):
        #self.token = "2bac4df9938c5c9f77c30cf33b0d71e29c0c79ac"
        user = User.objects.create(username="harsh")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
    
    def test_create_course_without_authentication(self):
        client = APIClient()
        url = reverse('api-courseCreate')
        data = {'name': 'java', 'information':'java tutorials'}
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_course(self):
        """
        Ensuring creation of new course object.
        """
        url = reverse('api-courseCreate')
        data = {'name': 'java', 'information':'java tutorials'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, 'java')

    def test_create_course_without_data(self):
        url = reverse('api-courseCreate')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_course_with_same_name(self):
        url = reverse('api-courseCreate')
        data = {'name': 'java', 'information':'java'}
        self.client.post(url, data, format='json')
        data1 = {'name': 'java', 'information':'java tutorials'}
        response = self.client.post(url, data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["name"][0], "course with this name already exists.")

    def test_course_list(self):
        url = reverse('api-courseCreate')
        data = {'name': 'java', 'information':'java tutorials'}
        response = self.client.post(url, data, format='json')
        url = reverse('api-courseList')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.count(), 1)

    def test_course_list_without_authentication(self):
        client = APIClient()
        url = reverse('api-courseList')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_single_course_desc(self):
        url = reverse('api-courseCreate')
        data = {'name': 'java', 'information':'java tutorials'}
        self.client.post(url, data, format='json')
        response1 = self.client.get("/api/course/course-detail/1/")
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_single_course_desc_without_auth(self):
        client = APIClient()
        response = client.get("/api/course/course-detail/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_single_course_desc_work_query(self):
        url = reverse('api-courseCreate')
        data = {'name': 'java', 'information':'java tutorials'}
        self.client.post(url, data, format='json')
        response = self.client.get("/api/course/course-detail/1/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["query_error"],"Please check url" )