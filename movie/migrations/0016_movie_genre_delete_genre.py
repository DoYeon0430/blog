# Generated by Django 4.2.1 on 2023-05-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_alter_genre_moviesubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('상업영화', '상업영화'), ('OTT 오리지널', 'OTT 오리지널'), ('드라마', '드라마')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='genre',
        ),
    ]
