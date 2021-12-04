import datetime as dt

from django.db.models import Count, Avg
from django.shortcuts import render

# Create your views here.
from Main.models import Building, Facility
from Review.models import Review, TagOnReview


def building_list(request):
    search = request.GET.get("search", "")

    bs = Building.objects.filter(name__icontains=search).values()

    buildings = []

    now_stamp = dt.datetime.now().hour * 60 + dt.datetime.now().minute

    for b in bs:
        try:
            hour, minute = b["open_time"].split(":")
            start_stamp = int(hour) * 60 + int(minute)
            hour, minute = b["close_time"].split(":")
            end_stamp = int(hour) * 60 + int(minute)

            if start_stamp < now_stamp < end_stamp:
                state = "open"
            else:
                state = "close"

        except:
            state = ""

        b = dict(b)

        b.setdefault("status", state)

        buildings.append(b)

    context = {
        "buildings": buildings,
        "search": search
    }

    return render(request, "Main/buildings.html", context=context)


def building_info(request, building_id):
    building = Building.objects.get(id=building_id)
    facilities = Facility.objects.filter(building=building)

    facilities = facilities.annotate(star=Avg('review__stars'))

    reviews = Review.objects.filter(building_id=building_id, facility__isnull=True).order_by("-create_date")

    tags = list(
        TagOnReview.objects.filter(review__building=building_id).values("tag").
            annotate(count=Count("id")).values("tag", "count")
    )

    tags.sort(key=lambda x: x["count"], reverse=True)

    tags = list(map(lambda x: x["tag"], tags[:5]))

    if reviews:
        star = sum(reviews.values_list("stars", flat=True)) / reviews.count()
    else:
        star = -1

    context = {
        "building": building,
        "facilities": facilities,
        "reviews": reviews,
        "star": star,
        "tags": tags
    }

    return render(request, "Main/building_info.html", context=context)

def facility_info(request, facility_id):
    facility = Facility.objects.get(id=facility_id)
    reviews = Review.objects.filter(facility_id=facility_id).order_by("-create_date")

    tags = list(
        TagOnReview.objects.filter(review__facility=facility_id).values("tag").
            annotate(count=Count("id")).values("tag", "count")
    )

    tags.sort(key=lambda x: x["count"], reverse=True)

    tags = list(map(lambda x: x["tag"], tags[:5]))

    if reviews:
        star = sum(reviews.values_list("stars", flat=True)) / reviews.count()
    else:
        star = -1

    context = {
        "facility": facility,
        "reviews": reviews,
        "star": star,
        "tags": tags
    }

    return render(request, "Main/facility_info.html", context=context)