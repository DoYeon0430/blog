# Generated by Django 4.2.1 on 2023-05-30 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0019_movie_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='meta',
            field=models.CharField(max_length=80),
        ),
    ]
