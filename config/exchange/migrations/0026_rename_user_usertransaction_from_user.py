# Generated by Django 4.2.11 on 2024-04-04 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0025_rename_currency_2_fk_orderbook_currency_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertransaction',
            old_name='user',
            new_name='from_user',
        ),
    ]
