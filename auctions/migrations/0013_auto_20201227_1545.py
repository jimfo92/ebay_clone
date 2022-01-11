# Generated by Django 3.1.1 on 2020-12-27 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20201227_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='auction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auctions.auctions'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]