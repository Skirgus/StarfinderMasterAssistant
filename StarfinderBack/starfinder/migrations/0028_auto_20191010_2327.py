# Generated by Django 2.2.2 on 2019-10-10 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starfinder', '0027_auto_20191010_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='feats',
            field=models.ManyToManyField(to='starfinder.Feat'),
        ),
        migrations.AddField(
            model_name='character',
            name='feats_pool',
            field=models.IntegerField(default=0),
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
    ]
