from django.db import models


# Create your models here.


class Building(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=20)
    open_time = models.CharField(max_length=5, blank=True)
    close_time = models.CharField(max_length=5, blank=True)
    major = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=45)
    spell = models.CharField(max_length=2)
    tel = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=20)
    open_time = models.CharField(max_length=5, blank=True)
    close_time = models.CharField(max_length=5, blank=True)
    location = models.CharField(max_length=45)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    tel = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.name
