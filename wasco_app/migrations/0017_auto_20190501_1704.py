# Generated by Django 2.1.7 on 2019-05-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0016_auto_20190501_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicedata',
            name='request_time',
            field=models.CharField(max_length=255),
        ),
    ]
