# Generated by Django 4.2.11 on 2024-03-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_rename_tags_tag_remove_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag_ids',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
