# Generated by Django 3.1 on 2021-01-17 03:37

from django.db import migrations, models
import django.db.models.deletion
import stream_django.activity


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_auto_20210116_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.member')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.member')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streamapp.item')),
            ],
            bases=(models.Model, stream_django.activity.Activity),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='account.member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='account.member')),
            ],
            options={
                'unique_together': {('user', 'target')},
            },
        ),
    ]
