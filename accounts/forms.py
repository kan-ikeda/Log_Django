# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150, 
        required=True, 
        help_text="文字、数字、@/./+/-/_ のみ使用可能です。",
        widget=forms.TextInput(attrs={
            "placeholder": "ユーザー名",
            'class' : 'form_input'
            })
    )

    password1 = forms.CharField(
        label="パスワード",
        help_text=("パスワードは8文字以上で、大文字、小文字、数字を含む必要があります。"),
        widget=forms.PasswordInput(attrs={""
        "placeholder": "パスワード",
        'class' : 'form_input'
        })
    )
    password2 = forms.CharField(
        label="パスワード確認",
        help_text="確認のため、上と同じパスワードを入力してください。",
        widget=forms.PasswordInput(attrs={
            "placeholder": "パスワード（再）",
            'class' : 'form_input'
            }),
    )

    email = forms.EmailField(
        max_length=254, 
        required=True, 
        help_text='有効なメールアドレスを入力してください。',
        widget=forms.EmailInput(attrs={
            "placeholder": "メールアドレス",
            'class' : 'form_input'
            })
        )

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-input'}),
            'avatar': forms.FileInput(attrs={'class': 'image_input'}),
        }


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