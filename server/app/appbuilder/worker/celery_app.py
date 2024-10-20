from server.app.worker.test import Celery
from config import CELERY_WORKER_NAME,CELERY_BACKEND_REDIS_URL,CELERY_BROKER_AMQP_URL,CELERY_CONFIG_TASK_ROUTES

celery_app = Celery(
    CELERY_WORKER_NAME,
    backend= CELERY_BACKEND_REDIS_URL,
    broker=CELERY_BROKER_AMQP_URL
)
celery_app.conf.task_routes = CELERY_CONFIG_TASK_ROUTES
celery_app.conf.update(task_track_started=True)