# Generated by Django 4.2.1 on 2023-06-03 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0031_alter_comment_django_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='code',
            field=models.CharField(choices=[('공군', '공군'), ('네트워크', '네트워크'), ('자격증', '자격증')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
