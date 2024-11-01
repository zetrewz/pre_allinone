from rest_framework.serializers import ModelSerializer

from base.models import Article


class ArticleListSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['user', 'content', 'created_at']


class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['content']
