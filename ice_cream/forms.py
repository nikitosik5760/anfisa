from django import forms
from django.utils.text import slugify

from .models import Comment, Review


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'content')
