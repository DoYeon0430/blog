# Generated by Django 4.2.1 on 2023-07-01 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0021_alter_movie_meta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='screening',
        ),
    ]