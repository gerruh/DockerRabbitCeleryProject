import os
from celery import Celery

RABBIT_USER = os.getenv("RABBITMQ_USER")
RABBIT_PASS = os.getenv("RABBITMQ_PASSWORD")

celery_app = Celery(
    "tasks",
    broker=f"amqp://{RABBIT_USER}:{RABBIT_PASS}@rabbitmq:5672//",
    backend="redis://redis:6379/0"
)

celery_app.autodiscover_tasks(["app"])