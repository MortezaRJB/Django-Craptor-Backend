# Generated by Django 4.2.11 on 2024-04-04 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0029_remove_userexternaltransaction_to_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userexternaltransaction',
            old_name='from_user',
            new_name='user',
        ),
    ]
