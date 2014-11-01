from django.contrib import admin
from yoamisafe.models import Incident
# Register your models here.
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['description', 'date', 'latitude', 'longitude']
admin.site.register(Incident, IncidentAdmin)
