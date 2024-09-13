# Generated by Django 5.1 on 2024-08-30 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('unique_url', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='ratings.conference')),
            ],
        ),
    ]
