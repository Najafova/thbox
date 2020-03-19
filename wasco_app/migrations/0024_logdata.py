# Generated by Django 2.2.1 on 2019-05-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0023_auto_20190518_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei_code', models.CharField(max_length=255)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('humidity', models.IntegerField(blank=True, null=True)),
                ('request_time', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]