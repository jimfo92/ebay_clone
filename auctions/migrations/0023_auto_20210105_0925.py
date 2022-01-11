# Generated by Django 3.1.1 on 2021-01-05 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20201229_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='user_created_auction',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bids',
            name='auction',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bids_auction', to='auctions.auctions'),
        ),
    ]