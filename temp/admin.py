from django.contrib import admin
from .models import Temperature, Sensor


class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('sensor_title', 'date', 'value')

    @staticmethod
    def sensor_title(obj):
        return obj.sensor.title


class SensorAdmin(admin.ModelAdmin):
    readonly_fields = ('uid',)
    list_display = ('title', 'uid',)


admin.site.register(Temperature, TemperatureAdmin)
admin.site.register(Sensor, SensorAdmin)
# Register your models here.
