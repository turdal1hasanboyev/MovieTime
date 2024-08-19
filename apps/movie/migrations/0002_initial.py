# Generated by Django 4.2.14 on 2024-08-19 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movieimage',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='movie.movie'),
        ),
        migrations.AddField(
            model_name='moviefile',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='movie.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 0}, related_name='actors', to='common.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='awards',
            field=models.ManyToManyField(blank=True, to='common.award'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': 0}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', related_query_name='movie', to='common.category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', related_query_name='movie', to='common.country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='common.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='regisseurs',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 1}, related_name='regisseurs', to='common.actor'),
        ),
        migrations.AddField(
            model_name='liked',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='movie.movie'),
        ),
        migrations.AddField(
            model_name='liked',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='liked_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_info', to='movie.movie'),
        ),
    ]
