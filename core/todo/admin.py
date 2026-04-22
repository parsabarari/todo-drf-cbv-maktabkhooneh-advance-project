from django.contrib import admin
from .models import TaskModel, Priority


admin.site.register(TaskModel)
admin.site.register(Priority)