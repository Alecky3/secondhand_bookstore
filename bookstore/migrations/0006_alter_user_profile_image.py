# Generated by Django 3.2.4 on 2021-09-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20210907_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank='True', null='True', upload_to='user_profiles/'),
        ),
    ]
