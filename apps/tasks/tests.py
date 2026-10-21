from django.test import TestCase

from utils.helpers import clean_title

from .models import Task
from .services import create_task, get_all_tasks


class TaskServiceTests(TestCase):
    def test_clean_title_strips_and_capitalizes(self):
        self.assertEqual(clean_title("  hello world "), "Hello world")

    def test_create_task_saves_clean_title(self):
        task = create_task("  buy milk ")
        self.assertEqual(task.title, "Buy milk")
        self.assertEqual(Task.objects.count(), 1)

    def test_get_all_tasks_returns_tasks(self):
        create_task("one")
        self.assertEqual(get_all_tasks().count(), 1)