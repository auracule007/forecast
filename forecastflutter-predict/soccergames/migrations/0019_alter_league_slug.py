# Generated by Django 4.2.7 on 2023-12-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0018_league_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='slug',
            field=models.SlugField(),
        ),
    ]
