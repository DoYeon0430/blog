# Generated by Django 4.2.1 on 2023-05-27 10:27

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0021_django_content_network_content_physics_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_physics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('physics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='engineer.physics')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='engineer.network')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_django',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('django', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='engineer.django')),
            ],
        ),
    ]
