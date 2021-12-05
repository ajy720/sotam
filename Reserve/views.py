from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Main.models import Building, Facility
from Reserve.ReserveForm import ReserveForm
from Reserve.models import Reserve


def building_list(request):
    buildings = Building.objects.all()

    context = {
        "buildings": buildings
    }

    return render(request, "Reserve/buildings.html", context=context)


def facility_list(request, building_id):
    if not request.user.is_authenticated:
        return redirect("user:login")

    building = Building.objects.get(id=building_id)

    facilities = Facility.objects.filter(building_id=building_id)
    if not request.user.is_admin:
        facilities = Facility.objects.filter(building_id=building_id, reserve__isnull=False).distinct()

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


def reserve_list(request, facility_id):
    facility = Facility.objects.get(id=facility_id)

    reserves = Reserve.objects.filter(facility_id=facility_id, user__isnull=True)

    context = {
        "reserves": reserves,
        "facility": facility
    }

    return render(request, "Reserve/reserve_list.html", context=context)


def reserve(request):
    if request.method == "POST":
        reserve = request.POST.get("reserve")

        try:
            reserve = Reserve.objects.get(id=reserve)

            reserve.user = request.user

            reserve.save()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)


