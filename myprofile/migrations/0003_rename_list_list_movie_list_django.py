# Generated by Django 4.2.1 on 2023-05-18 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_alter_genre_moviesubject'),
        ('engineer', '0021_django_content_network_content_physics_content'),
        ('myprofile', '0002_remove_list_mywork_list_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='List',
            new_name='List_movie',
        ),
        migrations.CreateModel(
            name='List_django',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('django', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineer.django')),
            ],
        ),
    ]