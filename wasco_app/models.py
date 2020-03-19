from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class DeviceData(models.Model):
    imei_code = models.CharField(_("Cihaz ID"),max_length=255)
    battery = models.FloatField(_("Temperatur"),blank=True, null=True)
    bin_state = models.IntegerField(_("Rütubət"),blank=True, null=True)
    request_time = models.CharField(_("Sorğu zamanı"),max_length=255)

    def __str__(self):
        return "{} {} {} {}".format(self.imei_code, self.battery, 
                                    self.bin_state, self.request_time)

    class Meta:
        verbose_name = "Device data"
        verbose_name_plural = "Device data"

    def device_icon(self):
        if self.bin_state>=0 and self.bin_state<25:
            return "/static/wasco/images/th.png"
        elif self.bin_state>=25 and self.bin_state<50:
            return "/static/wasco/images/th.png"
        elif self.bin_state>=50 and self.bin_state<75:
            return "/static/wasco/images/th.png"
        elif self.bin_state>=75:
            return "/static/wasco/images/th.png"

    
    def default(self):
        if self.bin_state>=0 and self.bin_state<25:
            return "/static/wasco/images/th.png"

class DeviceLimit(models.Model):
    up_limit = models.IntegerField(default=0)
    down_limit = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Device limit"
        verbose_name_plural = "Device limits"

class DeviceSettings(models.Model):
    imei_code = models.CharField(_("Cihaz ID"),max_length=255)
    latitude = models.FloatField(blank=True, null=True) 
    longitude = models.FloatField(blank=True, null=True) 

    def __str__(self):
        return "{} {} {}".format(self.imei_code, self.longitude, self.latitude)

    class Meta:
        verbose_name = "Device location"
        verbose_name_plural = "Device location"


class LogData(models.Model):
    imei_code = models.CharField(max_length=255)    
    battery = models.FloatField(blank=True, null=True)
    bin_state = models.IntegerField(blank=True, null=True)
    request_time = models.CharField(max_length=255)

    def __str__(self):
        return "{} {} {} {}".format(self.imei_code, self.battery, self.bin_state, self.request_time)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"