# Generated by Django 4.2.14 on 2024-08-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, max_length=225, null=True, unique=True),
        ),
    ]
