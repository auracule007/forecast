# Generated by Django 4.2.7 on 2023-12-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0024_alter_headtohead_notimp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headtohead',
            name='notimp',
            field=models.CharField(blank=True, default='', max_length=5, null=True),
        ),
    ]
