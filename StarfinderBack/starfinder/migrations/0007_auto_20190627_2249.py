# Generated by Django 2.2.2 on 2019-06-27 19:49

from django.db import migrations, models
import starfinder.models


class Migration(migrations.Migration):

    dependencies = [
        ('starfinder', '0006_auto_20190627_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilityvalue',
            name='ability',
            field=models.CharField(choices=[(starfinder.models.AbilityChoice('Сила'), 'Сила'), (starfinder.models.AbilityChoice('Ловкость'), 'Ловкость'), (starfinder.models.AbilityChoice('Выносливость'), 'Выносливость'), (starfinder.models.AbilityChoice('Интеллект'), 'Интеллект'), (starfinder.models.AbilityChoice('Мудрость'), 'Мудрость'), (starfinder.models.AbilityChoice('Харизма'), 'Харизма')], max_length=255),
        ),
        migrations.AlterField(
            model_name='gameclass',
            name='main_ability',
            field=models.CharField(choices=[(starfinder.models.AbilityChoice('Сила'), 'Сила'), (starfinder.models.AbilityChoice('Ловкость'), 'Ловкость'), (starfinder.models.AbilityChoice('Выносливость'), 'Выносливость'), (starfinder.models.AbilityChoice('Интеллект'), 'Интеллект'), (starfinder.models.AbilityChoice('Мудрость'), 'Мудрость'), (starfinder.models.AbilityChoice('Харизма'), 'Харизма')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='base_ability',
            field=models.CharField(choices=[(starfinder.models.AbilityChoice('Сила'), 'Сила'), (starfinder.models.AbilityChoice('Ловкость'), 'Ловкость'), (starfinder.models.AbilityChoice('Выносливость'), 'Выносливость'), (starfinder.models.AbilityChoice('Интеллект'), 'Интеллект'), (starfinder.models.AbilityChoice('Мудрость'), 'Мудрость'), (starfinder.models.AbilityChoice('Харизма'), 'Харизма')], max_length=255, null=True),
        ),
    ]
