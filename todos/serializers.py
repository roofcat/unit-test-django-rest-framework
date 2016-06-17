# -*- coding: utf-8 -*-


from rest_framework.serializers import ModelSerializer


from .models import Todo


class TodoSerializer(ModelSerializer):

	class Meta:
		model = Todo
		fields = (
			'id', 'created_at', 'title', 'body', 'finished_at', 'finished', 'user'
		)
		read_only_fields = ('user',)
