# Generated by Django 4.2.7 on 2023-12-04 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0025_alter_headtohead_notimp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='headhead',
        ),
        migrations.AddField(
            model_name='game',
            name='firstteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstname', to='soccergames.headtohead'),
        ),
        migrations.AddField(
            model_name='game',
            name='secondteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondname', to='soccergames.headtohead'),
        ),
    ]