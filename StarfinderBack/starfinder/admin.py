from django.contrib import admin
from .models import Race, RaceDescription, RacePlayingFor, SubRace
# Register your models here.

admin.site.register(Race)
admin.site.register(RaceDescription)
admin.site.register(RacePlayingFor)
admin.site.register(SubRace)