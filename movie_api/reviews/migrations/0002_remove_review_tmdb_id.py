# Generated by Django 5.1.6 on 2025-04-06 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='tmdb_id',
        ),
    ]
