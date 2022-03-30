from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content')

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article', 'created_at')
