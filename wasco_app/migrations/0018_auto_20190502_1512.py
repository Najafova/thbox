# Generated by Django 2.1.7 on 2019-05-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0017_auto_20190501_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicedata',
            name='down_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='up_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
