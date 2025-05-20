# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, ProfileForm, CustomAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ユーザー登録後に自動的にログイン
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mylog:log_create')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm



@login_required
def home(request):
    return render(request, 'mylog/log_create.html')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('mylog:mypage') # マイページにリダイレクト
        else:
            print(profile_form.errors)  # バリデーションエラーを表示
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {'profile_form': profile_form})

@login_required
def mypage(request):
    profile = request.user.profile
    return render(request, 'accounts/mypage.html', {'profile': profile})