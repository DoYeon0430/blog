# Generated by Django 4.2.1 on 2023-05-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
