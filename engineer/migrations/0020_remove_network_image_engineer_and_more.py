# Generated by Django 4.2.1 on 2023-05-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0019_django_hits_physics_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network_image',
            name='engineer',
        ),
        migrations.RemoveField(
            model_name='physics_image',
            name='engineer',
        ),
        migrations.AddField(
            model_name='django',
            name='photo',
            field=models.ImageField(default=1, upload_to='django/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='network',
            name='photo',
            field=models.ImageField(default=1, upload_to='network/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physics',
            name='photo',
            field=models.ImageField(default=1, upload_to='physics/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Django_Image',
        ),
        migrations.DeleteModel(
            name='Network_Image',
        ),
        migrations.DeleteModel(
            name='Physics_Image',
        ),
    ]
