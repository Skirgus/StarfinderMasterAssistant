from django.db import models
from .choices import AbilityChoice, CharacterPropertiesChoice
   

class RuleChoice(Enum):
    """Операция"""
    at_least = "Не менее"
    less = "Меньше"
    must_be = "Должно быть"
    must_be_absent = "Должно отсутствовать"


class Feat(models.Model):
    """Черта"""
    
    All = 'All'
    Any = 'Any'
    PREREQUEST_UNION_RULE_CHOICES = (
        (All, 'Все'),
        (Any, 'Хотябы один')
    )
    title = models.CharField(max_length=255,choices=PREREQUEST_UNION_RULE_CHOICES, default=All) # заголовок
    name = models.CharField(max_length=255) # название черты
    benefit = models.TextField() # описание преимущества
    normal = models.TextField(null=True, blank=True) # чего лишается персонаж, если не взята эта черта
    special = models.TextField(null=True, blank=True) # примечание
    is_combat = models.BooleanField(default=False) # признак боевой черты

    def __str__(self):
        return self.name 


class FeatPrerequest(models.Model):
    """Требования к черте"""
    description = models.CharField(max_length=255) # описание
    feat = models.ForeignKey('Feat', on_delete=models.CASCADE) # черта для которой действует правило
    required_feat = models.ForeignKey('Feat', on_delete=models.PROTECT, null=True, blank=True) # требуемая черта
    ability = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in AbilityChoice], null=True, blank=True)  # характеристика
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT, null=True, blank=True) # навык
    game_class = models.ForeignKey('GameClass', on_delete=models.PROTECT, null=True, blank=True) # класс
    character_property = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in CharacterPropertiesChoice], null=True, blank=True)  # свойство персонажа  
    value = models.IntegerField(null=True, blank=True) # значение
    rule = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in RuleChoice])  # характеристика