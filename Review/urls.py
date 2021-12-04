
from django.contrib import admin
from django.urls import path, include

from Review import views

app_name = "review"

urlpatterns = [
    path("building/<int:building_id>/create", views.create_review, name="createBuildingReview"),
    path("facility/<int:facility_id>/create", views.create_review, name="createFacilityReview"),
]
