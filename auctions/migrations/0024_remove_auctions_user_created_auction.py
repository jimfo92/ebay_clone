# Generated by Django 3.1.1 on 2021-01-05 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20210105_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctions',
            name='user_created_auction',
        ),
    ]
