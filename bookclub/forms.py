from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author','synopsis','published_year','book_cover','isbn_number')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('review_title','text',)
