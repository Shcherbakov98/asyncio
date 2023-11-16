"""Вызов асинхронного кода из синхронного представления"""
from asgiref.sync import async_to_sync
from functools import partial
from chapter_9.listing_9_11 import make_request
from django.shortcuts import render


def requests_view_sync(request):
    url: str = request.GET['url']
    request_num: int = int(request.GET['request_num'])
    context = async_to_sync(partial(make_request, url, request_num))()
    return render(request, 'async_api/requests.html', context)
