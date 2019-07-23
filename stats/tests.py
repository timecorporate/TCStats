from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from stats.models import User as UserTG
# Channels, Groups
# from stats.serializers import *


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testUsername", "email": "test@email.com",
                "password1": "testPassword", "password2": "testPassword"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserViewSetTestCase(APITestCase):
    list_url = reverse("user-list")

    def setUp(self):
        self.user = User.objects.create_user(username='testuser12',
                                             password='12345')
        self.token = Token.objects.create(user=self.user)
        self.userTG = UserTG.objects.create(telegram_id=12345688,
                                            first_name="test-user",
                                            last_name="test-user",
                                            username="test-user")
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_user_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail_retrieve(self):
        data = {"telegram_id": self.userTG.telegram_id}
        response = self.client.get(reverse('user-detail', kwargs=data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["telegram_id"], self.userTG.telegram_id)

    def test_profile_update(self):
        data = {"telegram_id": self.userTG.telegram_id}
        response = self.client.put(reverse('user-detail', kwargs=data),
                                   {"telegram_id": self.userTG.telegram_id,
                                    "username": self.userTG.username,
                                    "first_name": "test-user2",
                                    "last_name": "test-user2"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {"id": 1,
                          "telegram_id": self.userTG.telegram_id,
                          "username": self.userTG.username,
                          "first_name": "test-user2",
                          "last_name": "test-user2"})
# todo add test profile
