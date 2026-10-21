from django.db import models

from core.constants import TASK_STATUS_CHOICES, TASK_STATUS_PENDING


class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=TASK_STATUS_CHOICES,
        default=TASK_STATUS_PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
