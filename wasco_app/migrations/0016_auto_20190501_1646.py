# Generated by Django 2.1.7 on 2019-05-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0015_auto_20190501_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicedata',
            name='request_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
