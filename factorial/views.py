from django.http import HttpResponse
import logging
from .tasks import factorial


def front_factorial(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        return Http404()
    fact_resp = factorial.delay(offset).get()
    html = "<html><body>factorial of {} is {}</body></html>".format(offset, fact_resp)
    return HttpResponse(html)
