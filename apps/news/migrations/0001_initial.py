# Generated by Django 4.2.14 on 2024-08-21 03:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MovieNews',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('slug', models.SlugField(blank=True, max_length=225, null=True, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie_news')),
                ('premiere_date', models.DateField(blank=True, null=True)),
                ('trailer', models.URLField(blank=True, null=True, unique=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('actor', models.ManyToManyField(blank=True, limit_choices_to={'type': 0}, related_name='newsactors', to='common.actor')),
                ('category', models.ForeignKey(blank=True, limit_choices_to={'status': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movienews', related_query_name='moviesnews', to='common.category')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.country')),
                ('ganres', models.ManyToManyField(blank=True, to='common.genre')),
                ('regisseurs', models.ManyToManyField(blank=True, limit_choices_to={'type': 1}, related_name='newsregisseurs', to='common.actor')),
                ('tags', models.ManyToManyField(blank=True, to='news.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
