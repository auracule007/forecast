# Generated by Django 4.2.7 on 2023-11-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0008_alter_games_g_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='g_country',
        ),
        migrations.RemoveField(
            model_name='games',
            name='g_league',
        ),
    ]
