# -*- coding: utf-8 -*-


import json


from django.contrib.auth.models import User
from django.test import TestCase


from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


from .models import Todo


class TokenAuthUserTest(TestCase):

    def setUp(self):
        self.username = 'usuario'
        self.email = 'usuario@gmail.com'
        self.password = 'secreto'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.user.save()
        self.client = APIClient()

    def test_create_token_auth(self):
        data = {
            "username": "usuario",
            "password": "secreto"
        }
        response = self.client.post('/api-auth/', json.dumps(data), content_type="application/json")
        print response
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoTest(TestCase):

    def setUp(self):
        self.username = 'usuario'
        self.email = 'usuario@gmail.com'
        self.password = 'secreto'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.user.save()
        self.client = APIClient()

    def test_get_empty_todo_list(self):
        token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)
        request = self.client.get("/todos/", {}, format="json")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_todo_list(self):
        todo = Todo.objects.create(
            title = "hacer tarea",
            body = "terminar modulo django",
            user = self.user,
        )
        todo.save()
        token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)
        request = self.client.get("/todos/", {}, format="json")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
