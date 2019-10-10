from django.contrib import admin
from .models import Race, RaceDescription, RacePlayingFor, Subrace
from .models import Alignment, Deity, Theme, GameClass, Skill, World, Language
from .ruleModels import RaceRulesActingOnCharLevelUp, ThemeRulesActingOnCharLevelUp, ClassRulesActingOnCharLevelUp,SubRaceRulesActingOnCharLevelUp
from .ruleModels import ThemeClassSkills, ClassSkills
from .equipment import BaseEquipment, WeaponCategory, WeaponType, CriticalEffect, WeaponSpecial, Weapon, ArmorType, Armor
from .feat import Feat, FeatPrerequest

# Register your models here.

admin.site.register(Race)
admin.site.register(RaceDescription)
admin.site.register(RacePlayingFor)
admin.site.register(Language)
admin.site.register(Subrace)
admin.site.register(Alignment)
admin.site.register(Deity)
admin.site.register(Theme)
admin.site.register(GameClass)
admin.site.register(Skill)
admin.site.register(World)
admin.site.register(RaceRulesActingOnCharLevelUp)
admin.site.register(ThemeRulesActingOnCharLevelUp)
admin.site.register(ClassRulesActingOnCharLevelUp)
admin.site.register(SubRaceRulesActingOnCharLevelUp)
admin.site.register(ThemeClassSkills)
admin.site.register(ClassSkills)
admin.site.register(BaseEquipment)
admin.site.register(WeaponCategory)
admin.site.register(WeaponType)
admin.site.register(CriticalEffect)
admin.site.register(WeaponSpecial)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Feat)
admin.site.register(FeatPrerequest)
