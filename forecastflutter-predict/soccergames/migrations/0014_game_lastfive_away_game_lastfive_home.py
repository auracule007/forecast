# Generated by Django 4.2.7 on 2023-11-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0013_alter_game_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='lastfive_away',
            field=models.CharField(default='WWWWW', max_length=5),
        ),
        migrations.AddField(
            model_name='game',
            name='lastfive_home',
            field=models.CharField(default='LLLLL', max_length=5),
        ),
    ]