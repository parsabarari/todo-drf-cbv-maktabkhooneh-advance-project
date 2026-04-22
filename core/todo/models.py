from django.db import models


class TaskModel(models.Model):
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    priority = models.ForeignKey('Priority', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Priority(models.Model):
    title = models.CharField(max_length=50)
    level = models.IntegerField(help_text="the higher number is the task is more important")

    def __str__(self):
        return f"{self.title} ({self.level})"