# Generated by Django 4.2.11 on 2024-04-01 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0016_cryptocurrencytype_usertransaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertransaction',
            old_name='crypto_address',
            new_name='from_address',
        ),
        migrations.AddField(
            model_name='ethaccounts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default='ea7fa008-96d1-46f3-8448-f09931224389', on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertransaction',
            name='user',
            field=models.ForeignKey(default='ea7fa008-96d1-46f3-8448-f09931224389', on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
