from django.shortcuts import render
from django.http import JsonResponse
from .models import Temperature
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def temp(request):
    if request.method == 'POST':
        Temperature(value=request.POST.get("temperature")).save()
        return JsonResponse({"ACK": ""})
    else:
        return JsonResponse({"temperatures": [{"date": temperature.date, "value": temperature.value} for temperature in Temperature.objects.all()]})
