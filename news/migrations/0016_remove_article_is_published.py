# Generated by Django 5.1.5 on 2025-02-19 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_remove_article_favorites_favoritearticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_published',
        ),
    ]
