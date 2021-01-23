# Generated by Django 3.1 on 2021-01-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20210118_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='occurence',
            field=models.CharField(choices=[('M', 'Monthly'), ('D', 'Daily'), ('Y', 'Yearly'), ('W', 'Weekly')], default='Weekly', max_length=250),
        ),
    ]
