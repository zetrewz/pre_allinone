# Generated by Django 5.1.2 on 2024-11-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
