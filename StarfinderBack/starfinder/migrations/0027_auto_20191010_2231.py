# Generated by Django 2.2.2 on 2019-10-10 19:31

from django.db import migrations, models
import django.db.models.deletion
import starfinder.feat


class Migration(migrations.Migration):

    dependencies = [
        ('starfinder', '0026_auto_20191008_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('benefit', models.TextField()),
                ('normal', models.TextField(blank=True, null=True)),
                ('special', models.TextField(blank=True, null=True)),
                ('is_combat', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='subrace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='starfinder.Subrace'),
        ),
        migrations.AlterField(
            model_name='subracerulesactingoncharlevelup',
            name='subrace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rulesactingoncharlevelup', to='starfinder.Subrace'),
        ),
        migrations.CreateModel(
            name='FeatPrerequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('union_rule', models.CharField(choices=[('And', 'И'), ('Or', 'Или')], default=starfinder.feat.PrerequestUnionChoice('И'), max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('ability', models.CharField(blank=True, choices=[('STR', 'Сила'), ('DEX', 'Ловкость'), ('CON', 'Выносливость'), ('INT', 'Интеллект'), ('WIS', 'Мудрость'), ('CHA', 'Харизма')], max_length=255, null=True)),
                ('character_property', models.CharField(blank=True, choices=[('basic_attack_bonus', 'Базовый модификатор атаки'), ('basic_fortitude', 'Базовая стойкость'), ('basic_reflex', 'Базовая реакция'), ('basic_will', 'Базовая воля'), ('hit_points', 'Пункты здоровья'), ('stamina_points', 'Пункты живучести'), ('resolve_points', 'Пункты решимости'), ('ability_pool', 'Очки характеристик доступные для распределения'), ('skill_points_pool', 'Очки навыков доступные для распределения')], max_length=255, null=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('rule', models.CharField(choices=[('at_least', 'Не менее'), ('less', 'Меньше'), ('must_be', 'Должно быть'), ('must_be_absent', 'Должно отсутствовать')], max_length=255)),
                ('feat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prerequests', to='starfinder.Feat')),
                ('required_feat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='starfinder.Feat')),
                ('skill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='starfinder.Skill')),
            ],
        ),
    ]