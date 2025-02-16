from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(stuname="John Doe", email="john@example.com")

    def test_student_creation(self):
        """Test if a student instance is created correctly"""
        self.assertEqual(self.student.stuname, "John Doe")
        self.assertEqual(self.student.email, "john@example.com")

    def test_str_representation(self):
        """Test the string representation of the model"""
        self.assertEqual(str(self.student), self.student.stuname)

class StudentAPITest(APITestCase):
    def setUp(self):
        self.student1 = Student.objects.create(stuname="Alice", email="alice@example.com")
        self.student2 = Student.objects.create(stuname="Bob", email="bob@example.com")

    def test_get_student_list(self):
        """Test retrieving the list of students"""
        url = reverse('student-list')  # Ensure your URL name is 'student-list' in urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Expecting 2 students

    def test_student_list_content(self):
        """Check if the correct students are returned"""
        url = reverse('student-list')
        response = self.client.get(url)
        students = [student['stuname'] for student in response.data]
        self.assertIn("Alice", students)
        self.assertIn("Bob", students)
