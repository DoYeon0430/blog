# Generated by Django 4.2.1 on 2023-05-30 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0008_rename_meta_mywork_metaname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mywork',
            old_name='metaname',
            new_name='meta',
        ),
    ]
