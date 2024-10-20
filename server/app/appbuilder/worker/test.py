from time import sleep
from fastapi import FastAPI, BackgroundTasks 
from celery.result import AsyncResult
from ...celery_app import celery_app
from celery import shared_task


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    for i in range(1, 11):
        sleep(1)
        
    return f"test task return {word}"