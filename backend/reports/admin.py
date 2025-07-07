from django.contrib import admin
from .models import AccidentReport


@admin.register(AccidentReport)
class AccidentReportAdmin(admin.ModelAdmin):
    list_display = (
        'datetime',
        'latitude',
        'longitude',
        'number_of_casualties',
        'number_of_vehicles',
        'severity_score',
        'is_approved',
    )

    list_filter = (
        'is_approved',
        'weather_conditions',
        'light_conditions',
        'road_surface_conditions',
    )

    search_fields = (
        'weather_conditions',
        'vehicle_types_involved',
        'police_force',
    )
