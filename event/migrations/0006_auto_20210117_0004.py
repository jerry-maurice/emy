# Generated by Django 3.1 on 2021-01-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20210116_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='occurence',
            field=models.CharField(choices=[('D', 'Daily'), ('Y', 'Yearly'), ('W', 'Weekly'), ('M', 'Monthly')], default='Weekly', max_length=250),
        ),
    ]