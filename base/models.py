from django.contrib.auth import get_user_model
from django.db.models import Model, ForeignKey, CASCADE, TextField
from django.db.models.fields import DateTimeField

User = get_user_model()


class Article(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='articles')
    content = TextField(max_length=1000)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
