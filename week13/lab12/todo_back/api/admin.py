from django.contrib import admin
from api import models

admin.site.register(models.Task)
admin.site.register(models.TaskList)