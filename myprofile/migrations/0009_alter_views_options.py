# Generated by Django 4.2.1 on 2023-07-15 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0008_remove_list_movie_movie_remove_list_mywork_mywork_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='views',
            options={'verbose_name_plural': '전체 조회수'},
        ),
    ]