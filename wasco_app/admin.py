from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = ['imei_code', 'battery', 'bin_state', 
                    'request_time']
    search_fields = ['imei_code', 'battery', 'bin_state']

@admin.register(DeviceSettings)
class DeviceSettingsAdmin(admin.ModelAdmin):
    list_display = ['imei_code', 'latitude', 'longitude']
    search_fields = ['imei_code', 'latitude', 'longitude']
    list_filter = ['imei_code']


@admin.register(DeviceLimit)
class DeviceLimitAdmin(admin.ModelAdmin):
    list_display = ['up_limit', 'down_limit']

@admin.register(LogData)
class LogDataAdmin(admin.ModelAdmin):
    list_display = ['imei_code', 'battery', 'bin_state', 'request_time']
    search_fields = ['imei_code']
    list_filter = ['imei_code']