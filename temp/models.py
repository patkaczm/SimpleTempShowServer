from django.db import models


class Temperature(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(default=0.0)