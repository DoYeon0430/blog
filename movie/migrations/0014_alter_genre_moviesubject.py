# Generated by Django 4.2.1 on 2023-05-14 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_movie_content_alter_genre_moviesubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='moviesubject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
    ]
