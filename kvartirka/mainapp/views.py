import json
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


class ArticleView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def get(self, request, pk):
        comments = Comment.objects.filter(Q(article=pk) & Q(nesting_level__lte=3)).all()
        serializer = CommentSerializer(comments, many=True)
        return Response({"comments": serializer.data})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data,
                                       many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(status=400)


class CommentView(APIView):

    def post(self, request):
        serializer = CommentSerializer(data=request.data,
                                       many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if comment.nesting_level == 3:
            reg_exp = r'' + comment.uid + '.+'
            children_comments = Comment.objects.filter(Q(uid__regex=reg_exp)).all()
            serializer = CommentSerializer(children_comments, many=True)
            return Response({'children_comments': serializer.data})
        return Response({'error': 'bad nesting level comment, need be 3'}, status=400)
