from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .models import Temperature, Sensor
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


@csrf_exempt
def test(request):
    if request.method == 'POST':
        try:
            import ast
            data = ast.literal_eval(request.body.decode('utf-8'))
            print(data)

            try:
                sensor = Sensor.objects.get(uid=data['machine'])
            except Sensor.DoesNotExist:
                sensor = Sensor(uid=data['machine'], title="no title")
                sensor.save()

            Temperature(value=data['temperature'], sensor=sensor).save()

        except Exception as e:
            print(e)
            return JsonResponse({"ERR": "Sth goes wrong."})

    return JsonResponse({"ACK": ""})