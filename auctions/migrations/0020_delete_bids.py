# Generated by Django 3.1.1 on 2020-12-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_remove_bids_auction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bids',
        ),
    ]
