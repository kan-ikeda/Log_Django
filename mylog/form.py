from django import forms
from .models import Log, Comment

#日記作成用フォーム
class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('title', 'content', 'image', 'tags', 'is_public')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-title form_input',
                'placeholder': 'タイトル',
                'maxlength': 100,
            }),
            'image': forms.FileInput(attrs={
                'class': 'image_input',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-date',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-author',
                'readonly': 'readonly',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-content form_input',
                'rows': 10,
                'placeholder': 'キャプションを追加',
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-tags',
            }),
            'is_public': forms.CheckboxInput(attrs={
                'class': 'switch-input',
            }),
        }

# コメント投稿用フォーム
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'comment_content form_input',
                'rows': 3,
                'placeholder': 'コメントを追加',
            }),
        }