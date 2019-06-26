# Generated by Django 2.2.2 on 2019-06-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starfinder', '0005_abilityvalue_alignment_character_charactergameclass_characterskillvalue_deity_gameclass_skill_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alignment',
            name='good_evil',
            field=models.IntegerField(choices=[(0, 'Добрый'), (1, 'Нейтральный'), (2, 'Злой')], default=1),
        ),
        migrations.AlterField(
            model_name='alignment',
            name='lawfull_chaotic',
            field=models.IntegerField(choices=[(0, 'Принципиальный'), (1, 'Нейтральный'), (2, 'Хаотичный')], default=1),
        ),
    ]
