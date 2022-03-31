# Generated by Django 3.2.4 on 2021-09-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_mainsliderimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='bookstore.Category'),
        ),
        migrations.DeleteModel(
            name='Subcategories',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='subcategory',
            field=models.ManyToManyField(to='bookstore.Subcategory'),
        ),
    ]
