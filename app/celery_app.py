from celery import Celery

celery_app = Celery(
    "tasks",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/0"
)

celery_app.autodiscover_tasks(["app"])
