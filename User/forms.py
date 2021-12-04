from django.contrib.auth.forms import UserCreationForm

from .models import Users


class UserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('email', 'username', 'password1', 'password2', 'std_id', 'college', 'major', 'is_admin')
