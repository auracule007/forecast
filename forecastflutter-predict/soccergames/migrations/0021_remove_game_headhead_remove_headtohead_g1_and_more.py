# Generated by Django 4.2.7 on 2023-12-04 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0020_game_overone_game_overthree_game_overtwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='headhead',
        ),
        migrations.RemoveField(
            model_name='headtohead',
            name='g1',
        ),
        migrations.RemoveField(
            model_name='headtohead',
            name='g2',
        ),
        migrations.RemoveField(
            model_name='headtohead',
            name='g3',
        ),
        migrations.RemoveField(
            model_name='headtohead',
            name='g4',
        ),
        migrations.RemoveField(
            model_name='headtohead',
            name='g5',
        ),
        migrations.RemoveField(
            model_name='headtohead',
            name='team',
        ),
        migrations.AddField(
            model_name='headtohead',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='headtohead',
            name='first_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstteam', to='soccergames.team'),
        ),
        migrations.AddField(
            model_name='headtohead',
            name='result',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='headtohead',
            name='second_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondteam', to='soccergames.team'),
        ),
    ]