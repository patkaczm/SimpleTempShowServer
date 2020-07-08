from django.db import models


class Sensor(models.Model):
    uid = models.CharField(max_length=16)
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Temperature(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(default=0.0)
