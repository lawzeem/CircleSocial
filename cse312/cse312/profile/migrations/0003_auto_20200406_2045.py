# Generated by Django 2.1.2 on 2020-04-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.jpg', upload_to='profile'),
        ),
    ]