# Generated by Django 3.2.4 on 2021-09-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0012_auto_20210929_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='/media/user_profiles/user.svg', upload_to='user_profiles/'),
        ),
    ]