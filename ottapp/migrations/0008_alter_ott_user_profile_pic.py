# Generated by Django 5.1 on 2025-01-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0007_movies_thumbnail_movies_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ott_user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/profiles/'),
        ),
    ]
