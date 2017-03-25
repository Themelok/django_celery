from __future__ import absolute_import, unicode_literals
# from celery import shared_task
#
#
# @shared_task
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
from celery import Celery

app = Celery('tasks', backend='amqp://', broker='amqp://')


@app.task
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
