# Generated by Django 2.1.7 on 2019-05-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0021_auto_20190502_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicelimit',
            name='down_limit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='devicelimit',
            name='up_limit',
            field=models.CharField(max_length=255),
        ),
    ]