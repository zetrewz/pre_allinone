from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from base.models import Article, Comment


class ArticleListSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y, %H:%M:%S')

    class Meta:
        model = Article
        fields = ['user', 'content', 'created_at']


class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['content']


class ArticleUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['content']


# --------------------------------------------


class CommentListSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y, %H:%M:%S')

    class Meta:
        model = Comment
        fields = ['user', 'article', 'content', 'created_at']


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']


class CommentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
