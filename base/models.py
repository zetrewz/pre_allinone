from django.contrib.auth import get_user_model
from django.db.models import Model, ForeignKey, CASCADE, TextField, ManyToManyField, SET_NULL
from django.db.models.fields import DateTimeField, BooleanField, CharField

User = get_user_model()


class Article(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='articles')
    content = TextField(max_length=1000)
    topic = ForeignKey('Topic', on_delete=SET_NULL, blank=True, null=True, related_name='articles')
    likes = ManyToManyField(User, blank=True, related_name='likes')
    dislikes = ManyToManyField(User, blank=True, related_name='dislikes')
    is_draft = BooleanField(default=True)
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


class Topic(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
