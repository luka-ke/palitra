# Generated by Django 4.2.11 on 2024-03-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_article_tags'),
        ('modules', '0002_block_menu_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='articles',
            field=models.ManyToManyField(blank=True, to='content.article'),
        ),
    ]