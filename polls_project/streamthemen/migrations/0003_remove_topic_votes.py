# Generated by Django 3.1.6 on 2021-02-06 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamthemen', '0002_auto_20210206_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='votes',
        ),
    ]
