# Generated by Django 4.1.4 on 2022-12-18 11:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='disliked',
            field=models.ManyToManyField(blank=True, null=True, related_name='disliked', to=settings.AUTH_USER_MODEL),
        ),
    ]
