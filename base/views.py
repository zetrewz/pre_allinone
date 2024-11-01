from rest_framework.generics import ListAPIView, CreateAPIView

from base.models import Article
from base.serializers import ArticleListSerializer, ArticleCreateSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
