# Generated by Django 2.2.6 on 2019-12-25 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_service_watch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='serviceName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='watch',
            old_name='model_name',
            new_name='name',
        ),
    ]