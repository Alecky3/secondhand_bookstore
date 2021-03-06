# Generated by Django 3.2.4 on 2021-09-29 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0011_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookstore.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='mediauser_profiles/user.svg', upload_to='user_profiles/'),
        ),
    ]
