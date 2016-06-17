# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404


from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import Todo
from .serializers import TodoSerializer


class TodoApiView(APIView):
    serializer_class = TodoSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, id=None, format=None):
        if id is not None:
            todo = get_object_or_404(Todo, pk=id)
            response = self.serializer_class(todo, many=False)
        else:
            todos = Todo.objects.filter(user=request.user)
            response = self.serializer_class(todos, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        todo = self.serializer_class(data=request.data)
        print todo
        if todo.is_valid():
            print "es valido"
            todo.save(user=request.user)
            response = self.serializer_class(todo, many=False)
            return Response(response.data)
        else:
            print "no es valido"
            return Response(todo.errors)

    def patch(self, request, id=None, format=None):
        if id is not None:
            todo = Todo.finish_todo(id)
            return Response(todo.data)
        else:
            return Response({'message': 'To do has not been updated.'})
