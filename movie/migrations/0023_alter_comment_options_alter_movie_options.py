# Generated by Django 4.2.1 on 2023-07-15 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0022_remove_movie_screening'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '2. 댓글'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': '1. 영화 후기 포스팅'},
        ),
    ]