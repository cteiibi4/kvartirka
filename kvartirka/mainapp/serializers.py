from django.db.models import Q
from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Article

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class CommentSerializer(serializers.Serializer):
    article_id = serializers.IntegerField()
    parent_comment_id = serializers.IntegerField(required=False)
    body = serializers.CharField()
    id = serializers.IntegerField(required=False)
    uid = serializers.CharField(required=False, default='')
    nesting_level = serializers.IntegerField(required=False)

    class Meta:
        model = Comment

    def create(self, validated_data):
        parent_id = validated_data.get('parent_comment_id', None)
        if parent_id:
            parent_comment = Comment.objects.get(pk=parent_id)
            if parent_comment.article.id != validated_data.get('article_id', None):
                raise Exception
            validated_data['nesting_level'] = parent_comment.nesting_level + 1
            if parent_comment.uid == '':
                parent_comment.uid = str(parent_id)
                parent_comment.save()
            parent_uid = parent_comment.uid
            reg_ex = r'' + parent_uid + '.+'
            children_comments_count = Comment.objects.filter(Q(uid__regex=reg_ex)).count()
            new_last_index = children_comments_count + 1
            validated_data['uid'] = f'{parent_uid}.{new_last_index}'
        return Comment.objects.create(**validated_data)
