from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .models import Temperature
from django.views.decorators.csrf import csrf_exempt
import datetime

@csrf_exempt
def all_temp(request):
    return JsonResponse({"temperatures": [{"date": temperature.date, "value": temperature.value} for temperature in
                                          Temperature.objects.all()]})


@csrf_exempt
def set_temp(request, temperature=None):
    print(temperature)
    Temperature(value=temperature).save()
    return JsonResponse({"ACK": ""})


def show_temp(request):
    ret = []
    for temperature in Temperature.objects.filter(date__gt=datetime.datetime.today() - datetime.timedelta(days=1)):
        ret.append({'date': temperature.date.strftime('%x %X'),
                    'value': temperature.value})
    return render(request, "temp/show_temp.html", {'temperatures': ret})
