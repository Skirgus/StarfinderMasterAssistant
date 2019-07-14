from django.contrib import admin
from .models import Race, RaceDescription, RacePlayingFor, Subrace
from .models import Alignment, Deity, Theme, GameClass, Skill
from .models import RaceRulesActingOnCharLevelUp, ThemeRulesActingOnCharLevelUp, ClassRulesActingOnCharLevelUp

# Register your models here.

admin.site.register(Race)
admin.site.register(RaceDescription)
admin.site.register(RacePlayingFor)
admin.site.register(Subrace)
admin.site.register(Alignment)
admin.site.register(Deity)
admin.site.register(Theme)
admin.site.register(GameClass)
admin.site.register(Skill)
admin.site.register(RaceRulesActingOnCharLevelUp)
admin.site.register(ThemeRulesActingOnCharLevelUp)
admin.site.register(ClassRulesActingOnCharLevelUp)