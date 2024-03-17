# Generated by Django 4.2.11 on 2024-03-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_alter_menu_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='menu',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
