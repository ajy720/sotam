
from django.contrib import admin
from django.urls import path, include

from Reserve import views


app_name = "reserve"
urlpatterns = [
    path("building/", views.building_list, name="building_list"),
    path("<int:building_id>/facility", views.facility_list, name="facility_list"),
    path("create/<int:facility_id>", views.create_reserve, name="create_reserve"),

]
