# Generated by Django 3.2 on 2023-06-14 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/storage/emulated/0/Blog-client/static/avatar.jpeg', upload_to=''),
        ),
    ]
