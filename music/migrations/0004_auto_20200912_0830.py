# Generated by Django 3.1.1 on 2020-09-12 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200912_0716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
    ]
