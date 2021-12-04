import pdb

from django.shortcuts import render, redirect

# Create your views here.
from Main.models import Building, Facility
from Reserve.ReserveForm import ReserveForm


def building_list(request):
    buildings = Building.objects.all()

    context = {
        "buildings": buildings
    }

    return render(request, "Reserve/buildings.html", context=context)


def facility_list(request, building_id):
    facilities = Facility.objects.filter(building_id=building_id)
    building = Building.objects.get(id=building_id)

    context = {
        "facilities": facilities,
        "building": building
    }

    return render(request, "Reserve/facilities.html", context=context)


def create_reserve(request, facility_id):
    facility = Facility.objects.get(id=facility_id)
    if request.method == "POST":
        d = {
            "facility": facility_id,
            "admin": request.user,
            "start": request.POST.get("start"),
            "end": request.POST.get("end"),
        }

        form = ReserveForm(d)
        if form.is_valid():
            form.save()

        return redirect("user:mypage")
    else:
        form = ReserveForm()

    context = {
        "form": form,
        "facility": facility
    }

    return render(request, "Reserve/create_reserve.html", context=context)
