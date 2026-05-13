import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()




@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from accounts.tasks import cleanup_done_tasks
    sender.add_periodic_task(10*60, cleanup_done_tasks.s(), name='cleanup done tasks every 10 minutes')
