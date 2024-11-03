from django.contrib.auth import get_user_model
from django.db.models import Model, ForeignKey, CASCADE, TextField, ManyToManyField
from django.db.models.fields import DateTimeField, BooleanField

User = get_user_model()


class Article(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='articles')
    content = TextField(max_length=1000)
    likes = ManyToManyField(User, blank=True, related_name='likes')
    dislikes = ManyToManyField(User, blank=True, related_name='dislikes')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} {self.pk}"


class Comment(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='comments')
    article = ForeignKey(Article, on_delete=CASCADE, related_name='comments')
    parent_comment = ForeignKey('self', on_delete=CASCADE, blank=True, null=True, related_name='child_comments')
    content = TextField(max_length=1000)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"article {self.article.pk} {self.user} pk: {self.pk}"
