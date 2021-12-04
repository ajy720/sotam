from django.forms import ModelForm

from .models import Reserve


class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = (
            "facility",
            "start",
            "end",
            "admin",
        )
