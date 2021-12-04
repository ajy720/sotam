import pdb

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from User.forms import UserForm


def signup(request):
    if request.method == "POST":
        post = request.POST

        form = UserForm(post)
        # pdb.set_trace()
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)

            return redirect('main:main')
            # 회원가입 후 해당 계정으로 로그인 후 메인화면으로 이동
    else:
        form = UserForm()

    return render(request, 'User/signup.html', {'form': form})
