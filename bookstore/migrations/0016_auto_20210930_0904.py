# Generated by Django 3.2.4 on 2021-09-30 06:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0015_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.user'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.DateField(default=datetime.datetime(2021, 9, 30, 9, 4, 10, 503853)),
        ),
    ]
