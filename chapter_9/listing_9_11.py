"""Асинхронное представление Django"""
import asyncio
from datetime import datetime
from aiohttp import ClientSession
from django.shortcuts import render
import aiohttp


async def get_url_details(session: ClientSession, url):
    start_time = datetime.now()
    response = await session.get(url)
    response_body = await response.text()
    end_time = datetime.now()
    return {
        'status': response.status,
        'time': (end_time - start_time).microseconds,
        'body_length': len(response_body)
    }


async def make_request(url: str, request_num: int):
    async with aiohttp.ClientSession() as session:
        requests = [get_url_details(session, url) for _ in range(request_num)]
        results = await asyncio.gather(*requests, return_exceptions=True)
        failed_results = [str(result) for result in results if isinstance(result, Exception)]
        success_result = [result for result in results if not isinstance(result, Exception)]
        return {
            'failed_results': failed_results,
            'successful_results': success_result
        }


async def requests_view(request):
    url: str = request.GET['url']
    request_num: int = int(request.GET['request_num'])
    context = await make_request(url, request_num)
    return render(request, 'async_api/requests.html', context)
