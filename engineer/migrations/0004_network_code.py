# Generated by Django 4.2.1 on 2023-08-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0003_remove_network_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='code',
            field=models.CharField(choices=[('공군', '공군'), ('네트워크', '네트워크'), ('자격증', '자격증')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
