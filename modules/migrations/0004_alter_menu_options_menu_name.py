# Generated by Django 4.2.11 on 2024-03-16 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_alter_block_articles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]