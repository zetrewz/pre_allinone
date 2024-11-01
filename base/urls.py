from django.urls import path

from base.views import ArticleCreateView, ArticleListView

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
]
