# Generated by Django 2.2.2 on 2019-07-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starfinder', '0012_auto_20190709_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classrulesactingoncharlevelup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racerulesactingoncharlevelup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='themerulesactingoncharlevelup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
