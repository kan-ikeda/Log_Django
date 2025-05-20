# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='必須。有効なメールアドレスを入力してください。')

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date', 'avatar')


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'ユーザー名',
            'class' : 'form_input'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'パスワード',
            'class' : 'form_input'
        })