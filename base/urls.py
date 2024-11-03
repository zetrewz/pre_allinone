from django.urls import path

from base.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    ArticleLikeView, ArticleDislikeView, CommentCreateView, CommentListView, CommentUpdateView

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article-update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),
    path('like/<int:pk>/', ArticleLikeView.as_view(), name='article-like'),
    path('dislike/<int:pk>/', ArticleDislikeView.as_view(), name='article-dislike'),

    path('comment/list/<int:article_id>/', CommentListView.as_view(), name='comment-list'),
    path('comment/create/<int:article_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/create/parent/<int:article_id>/<int:parent_id>/', CommentCreateView.as_view(),
         name='comment-create-p'),
    path('comment/update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
]
