import pdb

from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
from Main.models import Building, Facility
from Review.ReviewForm import ReviewForm


def create_review(request, building_id=None, facility_id=None):
    if request.method == "POST":

        d = {
            "stars": request.POST.get("stars"),
            "comment": request.POST.get("comment"),
            "author": request.user,
        }

        if building_id:
            obj = Building.objects.get(id=building_id)
            d.setdefault("building", building_id)

        if facility_id:
            obj = Facility.objects.get(id=facility_id)
            d.setdefault("facility", facility_id)

        form = ReviewForm(d)

        if form.is_valid():
            form.save()

            if building_id:
                return redirect("main:building_info", building_id)

            if facility_id:
                return redirect("main:facility_info", facility_id)

        else:
            return HttpResponse(status=400)
