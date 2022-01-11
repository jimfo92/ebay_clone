# Generated by Django 3.1.1 on 2021-01-06 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_auto_20210106_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='user_who_made_last_successful_bid',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]