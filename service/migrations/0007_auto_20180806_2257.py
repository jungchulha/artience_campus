# Generated by Django 2.0.4 on 2018-08-06 13:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20180803_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 6, 22, 57, 57, 799995)),
        ),
        migrations.AddField(
            model_name='application',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Post'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.MyUser'),
        ),
    ]
