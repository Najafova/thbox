from django import forms 
from .models import *

class DeviceLimitForm(forms.ModelForm):
    class Meta:
        model = DeviceLimit
        fields = ("up_limit", "down_limit")
        labels = {"up_limit": "Yuxarı limit",
                  "down_limit": "Aşağı limit"}