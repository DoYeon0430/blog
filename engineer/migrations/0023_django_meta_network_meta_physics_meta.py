# Generated by Django 4.2.1 on 2023-05-30 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0022_comment_physics_comment_network_comment_django'),
    ]

    operations = [
        migrations.AddField(
            model_name='django',
            name='meta',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='network',
            name='meta',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physics',
            name='meta',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
