from django.contrib import admin
from .models import Baby, BabyMeasurement

# Register your models here.
admin.site.register(Baby)
admin.site.register(BabyMeasurement)