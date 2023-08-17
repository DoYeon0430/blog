# Generated by Django 4.2.1 on 2023-08-17 10:33

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Django',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('meta', models.CharField(max_length=130)),
                ('htmlcontent', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='django/')),
                ('code', models.CharField(choices=[('튜토리얼', '튜토리얼'), ('문법', '문법'), ('템플릿', '템플릿')], max_length=20)),
            ],
            options={
                'verbose_name_plural': '3. 디장고 포스팅',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('meta', models.CharField(max_length=130)),
                ('htmlcontent', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='network/')),
            ],
            options={
                'verbose_name_plural': '5. 네트워크 포스팅',
            },
        ),
        migrations.CreateModel(
            name='Physics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('meta', models.CharField(max_length=130)),
                ('htmlcontent', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='physics/')),
            ],
            options={
                'verbose_name_plural': '1. 물리학 포스팅',
            },
        ),
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
            options={
                'verbose_name_plural': '2. 물리학 댓글',
            },
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
            options={
                'verbose_name_plural': '6. 네트워크 댓글',
            },
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
            options={
                'verbose_name_plural': '4. 디장고 댓글',
            },
        ),
    ]
