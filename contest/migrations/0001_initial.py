# Generated by Django 3.1 on 2021-01-16 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Videolibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.URLField(blank=True)),
                ('roundNumber', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_video', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.IntegerField(blank=True, null=True)),
                ('confidence', models.IntegerField(blank=True, null=True)),
                ('choice', models.IntegerField(blank=True, null=True)),
                ('presentation', models.IntegerField(blank=True, null=True)),
                ('ontime', models.IntegerField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_rating', to='contest.videolibrary')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('liking', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_like', to='contest.videolibrary')),
            ],
        ),
    ]
