# Generated by Django 4.2.14 on 2024-08-31 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviefile',
            name='movie_id',
        ),
        migrations.AddField(
            model_name='moviefile',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_file', to='movie.movie'),
        ),
    ]
