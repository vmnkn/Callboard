from django import forms
from .models import Post, Comment
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Category not selected'
        self.fields['author'].empty_label = 'Author not selected'

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'photo',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        if text == title:
            raise ValidationError('Post`s text should not be identical to its title')
        return cleaned_data


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = [
            'user',
            'post',
            'text',
        ]

