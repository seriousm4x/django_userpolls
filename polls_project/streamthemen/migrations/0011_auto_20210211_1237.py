# Generated by Django 3.1.6 on 2021-02-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamthemen', '0010_bttvemote_ffzemote_twitchemote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bttvemote',
            name='_id',
            field=models.SlugField(),
        ),
    ]
