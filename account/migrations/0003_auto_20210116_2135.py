# Generated by Django 3.1 on 2021-01-17 02:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20210116_1345'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
