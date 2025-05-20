from django import forms
from .models import Log

#日記作成用フォーム
class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('title', 'content', 'image', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-title',
                'placeholder': 'タイトル',
                'maxlength': 100,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-image',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-date',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-author',
                'readonly': 'readonly',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-content',
                'rows': 10,
                'placeholder': 'キャプションを追加',
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-tags',
            }),
        }