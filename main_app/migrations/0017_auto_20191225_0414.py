# Generated by Django 2.2.6 on 2019-12-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20191225_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
