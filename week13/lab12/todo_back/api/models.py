from django.db import models
import datetime
from datetime import datetime as dt
from django.contrib.auth.models import User


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = dt.now()
    due_on = dt.now() + datetime.timedelta(days=1)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}: {}: {}: {}'.format(self.name, self.created_at, self.due_on, self.status, self.task_list)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at':self.created_at,
            'due_on': self.due_on
        }