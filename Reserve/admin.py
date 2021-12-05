from django.contrib import admin

# Register your models here.
from Reserve.models import Reserve


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ("facility",
                    "start",
                    "end",
                    "admin",
                    "user",)
