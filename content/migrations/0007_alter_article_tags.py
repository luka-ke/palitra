# Generated by Django 4.2.11 on 2024-03-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_remove_article_tag_ids_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='content.tag'),
        ),
    ]
