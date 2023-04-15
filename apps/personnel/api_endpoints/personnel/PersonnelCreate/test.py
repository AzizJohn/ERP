from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.personnel.models import Personnel, StaffType
from apps.users.models import CustomUser


class PersonnelCreateViewTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='test_username', password='test_password')
        self.client.login(username='test_username', password='test_password')

    def test_create_personnel(self):
        data = {
            'phone': '+998971234567',
            'full_name': 'John Doe',
            'position': 'Manager',
            'email': 'johndoe@example.com',
            'birthday': '1990-01-01',
            'date_of_employment': '2021-01-01',
            'salary': 50000,
            'bio': 'Some bio',
            'type': StaffType.STAFF,
        }
        url = reverse('personnel-create')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Personnel.objects.count(), 1)
        personnel = Personnel.objects.first()
        self.assertEqual(personnel.phone, '+998971234567')
        self.assertEqual(personnel.full_name, 'John Doe')
        self.assertEqual(personnel.position, 'Manager')
        self.assertEqual(personnel.email, 'johndoe@example.com')
        self.assertEqual(personnel.birthday.strftime('%Y-%m-%d'), '1990-01-01')
        self.assertEqual(personnel.date_of_employment.strftime('%Y-%m-%d'), '2021-01-01')
        self.assertEqual(personnel.salary, 50000)
        self.assertEqual(personnel.bio, 'Some bio')
        self.assertEqual(personnel.type, 'Staff')
