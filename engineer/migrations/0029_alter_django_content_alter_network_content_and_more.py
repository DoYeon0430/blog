# Generated by Django 4.2.1 on 2023-06-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0028_alter_django_meta_alter_network_meta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='network',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='physics',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
