from django.db import models

# Create your models here.
from Main.models import Facility, Building
from User.models import Users


class Review(models.Model):
    comment = models.TextField()
    stars = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment[:5]} {self.author} {self.building or self.facility}'


class TagOnReview(models.Model):
    tag = models.CharField(max_length=15)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def  __str__(self):
        return self.tag