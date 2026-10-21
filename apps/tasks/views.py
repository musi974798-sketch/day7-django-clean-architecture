from django.http import JsonResponse

from core.exceptions import TaskNotFoundError

from . import services


def task_list(request):
    tasks = services.get_all_tasks()
    data = [{"id": t.id, "title": t.title, "status": t.status} for t in tasks]
    return JsonResponse({"tasks": data})


def task_detail(request, task_id):
    try:
        task = services.get_task_by_id(task_id)
    except TaskNotFoundError as error:
        return JsonResponse({"error": str(error)}, status=404)
    return JsonResponse({"id": task.id, "title": task.title, "status": task.status})
