# Generated by Django 2.0.4 on 2018-09-19 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20180919_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 19, 15, 15, 52, 294610)),
        ),
    ]
