# Generated by Django 4.2.11 on 2024-03-16 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_article_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='test',
        ),
    ]
