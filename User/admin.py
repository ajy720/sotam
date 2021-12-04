from django.contrib import admin

# Register your models here.
from User.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    pass