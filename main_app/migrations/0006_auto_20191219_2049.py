# Generated by Django 2.2.6 on 2019-12-19 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20191219_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watch',
            old_name='strap_color',
            new_name='band_color',
        ),
        migrations.RenameField(
            model_name='watch',
            old_name='strap_type',
            new_name='band_type',
        ),
        migrations.RenameField(
            model_name='watch',
            old_name='strap_width',
            new_name='band_width',
        ),
    ]
