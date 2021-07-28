import os

from celery import Celery
import requests


# RABBITMQ_URL: str = os.environ['CELERY_RABBITMQ_URL']
REDIS_URL: str = os.environ['REDIS_URL']
app = Celery('tasks', broker=REDIS_URL)


@app.task
def count_to(n):
    print('RUNNING celery_demo::count_to')
    for i in range(n):
        print(i)


# Example 2
@app.task
def get_uri_contents(uri: str):
    return requests.get(uri).text

@app.task
def count_words(uri: str, text: str):
    count = len(text.split(" "))
    print(f"There are {count} words at {uri}.")
