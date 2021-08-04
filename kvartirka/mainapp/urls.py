from django.urls import path
from .views import ArticleView, CommentView


urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('article/<int:pk>', ArticleView.as_view()),
    path('comment/', CommentView.as_view()),
    path('comment/<int:pk>', CommentView.as_view()),
    ]
