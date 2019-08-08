import django
from django.db import models
from .choices import AbilityChoice, CharacterPropertiesChoice, OperationChoice

class BaseRule(models.Model):
    """Базовый класс для правил"""
    class Meta:
        abstract = True
    name = models.CharField(max_length=255, null=True, blank=True) # название правила
    description = models.TextField(null=True, blank=True) # описание правила

class RulesActingOnCharLevelUp(BaseRule):
    """Базовый класс для правил действующих на персонажа при повышении уровня"""
    class Meta:
        abstract = True
    level = models.IntegerField() # уровень при достижении которого срабатывает правило
    ability = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in AbilityChoice], null=True, blank=True)  # характеристика
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT, null=True, blank=True) # навык
    character_property = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in CharacterPropertiesChoice], null=True, blank=True)  # свойство персонажа  
    change_to = models.IntegerField() # значение на которое изменяется параметр
    operation = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in OperationChoice], null=True, blank=True)  # операция

class RaceRulesActingOnCharLevelUp(RulesActingOnCharLevelUp):
    """Правила расы действующие при повышении в уровне"""
    race = models.ForeignKey('Race',  related_name='rulesactingoncharlevelup', on_delete=models.CASCADE) # раса
    
    def __str__(self):
        return self.race.name + ' (' + self.name+ ')'

    
class ThemeRulesActingOnCharLevelUp(RulesActingOnCharLevelUp):
    """Правила темы действующие при повышении в уровне"""
    theme = models.ForeignKey('Theme',  related_name='rulesactingoncharlevelup', on_delete=models.CASCADE) # тема
    
    def __str__(self):
        return self.theme.name + ' (' + self.name+ ')'
    
    
class ClassRulesActingOnCharLevelUp(RulesActingOnCharLevelUp):
    """Правила класса действующие при повышении в уровне"""
    game_class = models.ForeignKey('GameClass',  related_name='rulesactingoncharlevelup', on_delete=models.CASCADE) # тема

    def __str__(self):
        return self.game_class.name + ' (' + self.name+ ')'

class RaceRulesActingOnCharLevelUp(RulesActingOnCharLevelUp):
    """Правила подрасы действующие при повышении в уровне"""
    subrace = models.ForeignKey('Subrace',  related_name='rulesactingoncharlevelup', on_delete=models.CASCADE) # подраса
    
    def __str__(self):
        return self.subrace.name + ' (' + self.name+ ')'


class SetClassSkill(BaseRule):
    """Базовый класс для правил устанавливающих классовый навык"""
    class Meta:
        abstract = True
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT, null=True, blank=True) # навык

class ThemeClassSkills(SetClassSkill):
    """Правила темыустанавливающие классовые навыки"""
    theme = models.ForeignKey('Theme',  related_name='set_class_skill_rules', on_delete=models.CASCADE) # тема
    
    def __str__(self):
        return self.theme.name + ' (' + self.name + ')'    
    
class ClassSkills(SetClassSkill):
    """Правила класса устанавливающие классовые навыки"""
    game_class = models.ForeignKey('GameClass',  related_name='set_class_skill_rules', on_delete=models.CASCADE) # класс

    def __str__(self):
        return self.game_class.name + ' (' + self.name + ')'