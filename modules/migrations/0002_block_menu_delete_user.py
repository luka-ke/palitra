# Generated by Django 4.2.11 on 2024-03-16 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_article_author'),
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('vizualType', models.CharField(choices=[('standard', 'STANDARD'), ('vertical', 'VERTICAL'), ('horizontal', 'HORIZONTAL')], max_length=20)),
                ('position', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=250)),
                ('display_title', models.BooleanField(default=True)),
                ('articles', models.ManyToManyField(related_name='Blocks', to='content.article')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=100)),
                ('is_external', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='content.category')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
