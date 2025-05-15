from django import forms
from .models import Log

#日記作成用フォーム
class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('title', 'date', 'content')