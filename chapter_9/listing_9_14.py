"""Представление sync_to_async_view"""
import asyncio
from functools import partial
from django.http import HttpResponse
from asgiref.sync import sync_to_async


def sleep(seconds: int):
    import time
    time.sleep(seconds)


async def sync_to_async_view(request):
    sleep_time: int = int(request.GET['sleep_time'])
    num_calls: int = int(request.GET['num_calls'])
    thread_sensitive: bool = request.GET['thread_sensitive'] == 'True'
    function = sync_to_async(partial(sleep, sleep_time), thread_sensitive=thread_sensitive)
    await asyncio.gather(*[function() for _ in range(num_calls)])
    return HttpResponse('')
