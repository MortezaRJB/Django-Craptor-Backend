# Generated by Django 4.2.11 on 2024-04-04 12:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0027_usertransaction_to_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserTransaction',
            new_name='UserExternalTransaction',
        ),
    ]
