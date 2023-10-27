# Generated by Django 4.2.6 on 2023-10-27 13:08

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
            name='todaymonologue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('theme', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('dialogue', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_username', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField()),
                ('profile_photo', models.ImageField(default='profile_img.png', upload_to='profile_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to='post_videos')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('no_of_views', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]