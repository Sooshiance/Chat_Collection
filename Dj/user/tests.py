from django.test import TestCase
from django.urls import reverse_lazy

from .models import User 


class LogInTest(TestCase):
    def setUp(self):
        self.login = reverse_lazy("user:login")
        self.credentials = {
            'phone': '09026386221',
            'password': '123'}
        User.objects.create(**self.credentials)
    
    def test_login(self):
        # send login data
        response = self.client.post(self.login, self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'])


class RegisterTest(TestCase):
    def setUp(self):
        self.register = reverse_lazy("user:register")
        self.credentials = {
        'phone': '09026386222',
        'username': 'username123',
        'password': 'Mypassword777',
        }
        User.objects.create_user(**self.credentials)
    
    def test_register(self):
        # send register data
        response = self.client.post(self.register, self.credentials, follow=True)
        # should be register now
        self.assertTrue(response.context['user'])
