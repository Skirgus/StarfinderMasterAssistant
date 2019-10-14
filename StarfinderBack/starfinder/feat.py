from django.db import models
from .choices import AbilityChoice, CharacterPropertiesChoice
from rest_framework import serializers
from enum import Enum
   

class RuleChoice(Enum):
    """Операция"""
    at_least = "Не менее"
    less = "Меньше"
    must_be = "Должно быть"
    must_be_absent = "Должно отсутствовать"

class PrerequestUnionChoice(Enum):
    """Правила объединения предусловий"""
    And = 'И'
    Or = 'Или'


class Feat(models.Model):
    """Черта"""
    name = models.CharField(max_length=255) # название черты
    benefit = models.TextField() # описание преимущества
    normal = models.TextField(null=True, blank=True) # чего лишается персонаж, если не взята эта черта
    special = models.TextField(null=True, blank=True) # примечание
    is_combat = models.BooleanField(default=False) # признак боевой черты

    def __str__(self):
        return self.name 


class FeatPrerequest(models.Model):
    """Требования к черте"""
    union_rule = models.CharField(max_length=255,choices=[(tag.name, tag.value) 
                            for tag in PrerequestUnionChoice], default=PrerequestUnionChoice.And) # условие объединения предусловий
    description = models.CharField(max_length=255) # описание
    feat = models.ForeignKey('Feat', related_name = 'prerequests', on_delete=models.CASCADE) # черта для которой действует правило
    required_feat = models.ForeignKey('Feat', on_delete=models.PROTECT, null=True, blank=True) # требуемая черта
    ability = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in AbilityChoice], null=True, blank=True)  # характеристика
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT, null=True, blank=True) # навык
    character_property = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in CharacterPropertiesChoice], null=True, blank=True)  # свойство персонажа  
    value = models.IntegerField(null=True, blank=True) # значение
    rule = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in RuleChoice])  # правило для выполнения условия
    def __str__(self):
        return self.feat.name + ' ' + self.description

class FeatPrerequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatPrerequest
        fields = ('id', 'description', 'union_rule')

class FeatListSerializer(serializers.ModelSerializer):
    prerequests = FeatPrerequestSerializer(many=True, read_only=True)
    class Meta:
        model = Feat
        fields = ('id', 'name', 'benefit', 'normal', 'special', 'prerequests')