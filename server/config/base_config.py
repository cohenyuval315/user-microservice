class ApplicationConfiguration:
    pass


ALLOWED_FILE_EXTENSIONS = {
    "txt", 
    "pdf", 
    "png", 
    "jpg", 
    "jpeg", 
    "gif"
}




CORS = {
    "allow_origins":["*"],
    "allow_credentials":True,
    "allow_methods":["*"],
    "allow_headers":["*"],
}
    
CELERY_WORKER_NAME = "worker"
CELERY_BACKEND_REDIS_URL = "redis://:password123@localhost:6379/0"
CELERY_BROKER_AMQP_URL = "amqp://user:bitnami@localhost:5672//"

CELERY_CONFIG_TASK_ROUTES = {
    "app.worker.celery_worker.test_celery": "test-queue"
}
