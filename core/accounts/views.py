from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests

@cache_page(6)
def cache_test(request):
    url = "https://api.nerkh.io/v1/prices/json/gold/"
    token = "yLTts14pJX_vWmAO6Wv4FwAm3xIUDteUEOl9HKd9F9Q="

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({
            "error": "API request failed",
            "status_code": response.status_code,
            "detail": response.text,
        }, status=response.status_code)
    