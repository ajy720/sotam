from django.db import models

# Create your models here.
from Main.models import Facility
from User.models import Users


class Reserve(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    admin = models.ForeignKey(Users, related_name="admin",on_delete=models.CASCADE)
    user = models.ForeignKey(Users, related_name="user",on_delete=models.CASCADE, null=True, blank=True)
