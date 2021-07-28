import os
import requests

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.brokers.redis import RedisBroker


# RABBITMQ_URL: str = os.environ['DRAMATIQ_RABBITMQ_URL']
# rabbitmq_broker = RabbitmqBroker(url=RABBITMQ_URL)
# dramatiq.set_broker(rabbitmq_broker)

REDIS_URL: str = os.environ['REDIS_URL']
redis_broker = RedisBroker(url=REDIS_URL)
dramatiq.set_broker(redis_broker)


# Example 1
@dramatiq.actor
def count_to(n):
    print('RUNNING dramatiq_demo::count_to')
    for i in range(n):
        print(i)


# Example 2
@dramatiq.actor
def get_uri_contents(uri: str):
    return requests.get(uri).text

@dramatiq.actor
def count_words(uri: str, text: str):
    count = len(text.split(" "))
    print(f"There are {count} words at {uri}.")
