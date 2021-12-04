
from django.contrib import admin
from django.urls import path, include

from Main import views


app_name = "main"
urlpatterns = [
    path("", views.building_list, name="building_list"),
    path("building/<int:building_id>", views.building_info, name="building_info"),
    path("facility/<int:facility_id>", views.facility_info, name="facility_info"),

]
