# Generated by Django 3.1.6 on 2021-02-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamthemen', '0009_auto_20210207_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='BTTVEmote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.PositiveIntegerField()),
                ('code', models.SlugField()),
                ('imageType', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='FFZEmote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.PositiveIntegerField()),
                ('name', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TwitchEmote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.PositiveIntegerField()),
                ('code', models.SlugField()),
            ],
        ),
    ]
