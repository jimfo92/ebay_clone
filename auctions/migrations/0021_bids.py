# Generated by Django 3.1.1 on 2020-12-29 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_delete_bids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_bid', models.IntegerField(default=0)),
                ('last_bid', models.IntegerField(default=0)),
            ],
        ),
    ]
