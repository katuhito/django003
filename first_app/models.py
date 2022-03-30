from unicodedata import name
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(verbose_name='本文')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='投稿日')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '記事'


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='名前')
    content = models.TextField(verbose_name='本文')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='投稿日')
    article = models.ForeignKey(to=Article, related_name='comments', on_delete=models.CASCADE, verbose_name='対象記事')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'コメント'
