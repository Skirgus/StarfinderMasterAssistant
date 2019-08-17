# Generated by Django 2.2.2 on 2019-08-11 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starfinder', '0017_auto_20190808_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
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
        migrations.AddField(
            model_name='character',
            name='languages',
            field=models.ManyToManyField(to='starfinder.Language'),
        ),
        migrations.AddField(
            model_name='race',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='starfinder.Language'),
        ),
        migrations.AddField(
            model_name='world',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='starfinder.Language'),
        ),
    ]