# Generated by Django 4.2.7 on 2023-11-28 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0010_rename_country_country_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]
