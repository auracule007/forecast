# Generated by Django 4.2.7 on 2023-11-27 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0009_remove_games_g_country_remove_games_g_league'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='league',
            old_name='l_country',
            new_name='country',
        ),
    ]
