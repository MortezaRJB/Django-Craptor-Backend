# Generated by Django 5.0.3 on 2024-03-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_rename_size_to_trade_order_size_remained'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Filled', 'Filled'), ('Active_Not_Filled', 'Active Not Filled'), ('Active_Partially_Filled', 'Active Partially Filled'), ('Cancelled_Not_Filled', 'Cancelled Not Filled'), ('Cancelled_Partially_Filled', 'Cancelled Partially Filled')], default='Cancelled_Not_Filled', max_length=50),
            preserve_default=False,
        ),
    ]
