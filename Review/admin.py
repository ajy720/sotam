from django.contrib import admin

# Register your models here.
from Review.models import Review, TagOnReview


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(TagOnReview)
class TagAdmin(admin.ModelAdmin):
    pass