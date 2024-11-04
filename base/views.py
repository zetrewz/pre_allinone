from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Article, Comment
from base.permissions import IsOwnerPermission
from base.serializers import ArticleListSerializer, ArticleCreateSerializer, ArticleUpdateSerializer, \
    CommentCreateSerializer, CommentListSerializer, CommentUpdateSerializer
from base.service import ArticleService

article_tag = extend_schema(tags=['Articles'])
comment_tag = extend_schema(tags=['Comments'])


@article_tag
class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_draft=False)


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


@article_tag
class ArticleLikeView(APIView):
    serializer_class = ArticleListSerializer

    def post(self, request, pk):
        service = ArticleService(pk, request.user)
        service.toggle_like()
        return Response({"detail": f"Like toggled."}, status=status.HTTP_200_OK)


@article_tag
class ArticleDislikeView(APIView):
    serializer_class = ArticleListSerializer

    def post(self, request, pk):
        service = ArticleService(pk, request.user)
        service.toggle_dislike()
        return Response({"detail": f"Dislike toggled."}, status=status.HTTP_200_OK)


# --------------------------------------------


@comment_tag
class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return self.queryset.filter(article_id=self.kwargs.get('article_id'))


@extend_schema(
    tags=['Comments'],
    parameters=[OpenApiParameter(name="parent_id", type=int, required=False)],
)
class CommentCreateView(APIView):
    serializer_class = CommentCreateSerializer

    def post(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        parent_id = request.query_params.get('parent_id')
        parent_comment = get_object_or_404(Comment, pk=parent_id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                user=self.request.user,
                article=article,
                parent_comment=parent_comment
            )
            return Response({"detail": "Comment created successfully"}, status=status.HTTP_200_OK)


@comment_tag
class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsOwnerPermission]

# --------------------------------------------


class TopicArticlesView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        return Article.objects.filter(topic__name=self.kwargs['name'])
