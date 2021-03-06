# Generated by Django 3.2.7 on 2021-09-19 05:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tube', '0003_auto_20210919_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='comment',
            field=models.ManyToManyField(related_name='video_comment', through='tube.VideoComment', to=settings.AUTH_USER_MODEL, verbose_name='コメント'),
        ),
    ]
