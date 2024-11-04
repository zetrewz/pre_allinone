from django.shortcuts import get_object_or_404

from base.models import Article


class ArticleService:
    def __init__(self, pk, user):
        self.article = get_object_or_404(Article, pk=pk)
        self.user = user

    def toggle_like(self):
        if self.article.dislikes.filter(pk=self.user.pk).exists():
            self.article.dislikes.remove(self.user)
        if self.article.likes.filter(pk=self.user.pk).exists():
            self.article.likes.remove(self.user)
        else:
            self.article.likes.add(self.user)

    def toggle_dislike(self):
        if self.article.likes.filter(pk=self.user.pk).exists():
            self.article.likes.remove(self.user)
        if self.article.dislikes.filter(pk=self.user.pk).exists():
            self.article.dislikes.remove(self.user)
        else:
            self.article.dislikes.add(self.user)
