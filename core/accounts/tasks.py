from celery import shared_task
from time import sleep




@shared_task
def cleanup_done_tasks():
    from todo.models import TaskModel
    deleted, _ = TaskModel.objects.filter(completed=True).delete()
    print(f'completed tasks deleted successfully: deleted={deleted}')