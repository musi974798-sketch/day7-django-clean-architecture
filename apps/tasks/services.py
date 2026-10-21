from core.exceptions import TaskNotFoundError
from utils.helpers import clean_title

from .models import Task


def create_task(title: str) -> Task:
    return Task.objects.create(title=clean_title(title))


def get_all_tasks():
    return Task.objects.all().order_by("-created_at")


def get_task_by_id(task_id: int) -> Task:
    try:
        return Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise TaskNotFoundError(f"Task {task_id} not found")
