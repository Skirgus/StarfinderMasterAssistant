# Generated by Django 2.2.2 on 2019-06-24 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starfinder', '0003_auto_20190623_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subraces', to='starfinder.Race')),
            ],
        ),
    ]
