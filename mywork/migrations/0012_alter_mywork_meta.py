# Generated by Django 4.2.1 on 2023-05-31 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0011_alter_mywork_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywork',
            name='meta',
            field=models.CharField(max_length=130),
        ),
    ]