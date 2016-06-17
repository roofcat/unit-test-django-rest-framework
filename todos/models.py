# -*- coding: utf-8 -*-


from __future__ import unicode_literals


from datetime import datetime


from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class Todo(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=120)
	body = models.TextField()
	finished_at = models.DateTimeField(null=True)
	finished = models.BooleanField(default=False)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	@classmethod
	def finish_todo(self, id):
		todo = get_object_or_404(Todo, pk=id)
		todo.finished_at = datetime.now()
		todo.finished = True
		return todo
