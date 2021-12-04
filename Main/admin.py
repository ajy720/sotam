from django.contrib import admin

# Register your models here.
from Main.models import Building, Facility


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'spell', 'open_time', 'close_time', 'major')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('building', 'name', 'open_time', 'close_time')
