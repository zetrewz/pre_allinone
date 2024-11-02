from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from base.models import Article
from base.permissions import IsOwnerPermission
from base.serializers import ArticleListSerializer, ArticleCreateSerializer, ArticleUpdateSerializer

article_tag = extend_schema(tags=['Articles'])


@article_tag
class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


@article_tag
class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@article_tag
class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


@article_tag
class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleUpdateSerializer
    permission_classes = [IsOwnerPermission]


@article_tag
class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsOwnerPermission]
