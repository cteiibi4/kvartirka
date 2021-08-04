from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    body = models.TextField()
    uid = models.CharField(max_length=255, default='0')
    nesting_level = models.IntegerField(default=0)
