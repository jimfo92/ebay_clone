# Generated by Django 3.1.1 on 2020-12-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201221_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='image_url',
            field=models.URLField(default=''),
        ),
    ]