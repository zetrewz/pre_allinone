from django.urls import path

from base.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article-update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),
]
