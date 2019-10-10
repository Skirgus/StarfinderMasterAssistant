from django.db import models
from django.db.models import Q
from itertools import chain
from django.db.models.signals import post_save, pre_save
from .choices import AbilityChoice, SexChoice, OperationChoice, CharacterPropertiesChoice
from .models import Language
from .feat import Feat

class Character(models.Model): 
    """Персонаж""" 
    user = models.ForeignKey('auth.User',  related_name='characters', on_delete=models.CASCADE)      
    name = models.CharField(max_length=255, unique=True) # имя персонажа
    portrait = models.ImageField(upload_to='character_portraits/', null=True, blank=True) # портрет персонажа
    gender = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in SexChoice])  # пол
    description = models.TextField(null=True, blank=True) # описание
    race = models.ForeignKey('Race',  related_name='characters', on_delete=models.CASCADE) # раса
    subrace = models.ForeignKey('Subrace', null=True, blank=True, on_delete=models.SET_NULL) #под раса
    theme = models.ForeignKey('Theme',  related_name='characters', on_delete=models.CASCADE) # тема
    alignment = models.ForeignKey('Alignment', on_delete=models.PROTECT) # мировозрение
    deity = models.ForeignKey('Deity', null=True, blank=True, on_delete=models.SET_NULL) # божество
    home_world = models.ForeignKey('World', null=True, blank=True, on_delete=models.SET_NULL) # родной мир
    ability_pool = models.IntegerField(default=0) # очки характеристик доступные для распределения
    skill_points_pool = models.IntegerField(default=0) # очки навыков доступные для распределения
    distributed_skill_points = models.IntegerField(default=0) # очки навыков вложенные в навыки (это поле надо явно менять на клиенте, 
    # только так будет уверенность что очко вложенной в навык вложенно пользователем из пула очков навыков) на основе него можно будет рассчитать,
    # сколько очков надо добавить при изменении интеллекта
    level = models.IntegerField() # уровень
    basic_attack_bonus = models.IntegerField(default=0) # базовый модификатор атаки
    basic_fortitude = models.IntegerField(default=0) # базовая стойкость
    basic_reflex = models.IntegerField(default=0) # базовая реакция
    basic_will = models.IntegerField(default=0) # базовая воля
    hit_points = models.IntegerField(default=0) # пункты здоровья
    stamina_points = models.IntegerField(default=0) # пункты живучести
    resolve_points = models.IntegerField(default=0) # пункты решимости 
    languages = models.ManyToManyField(Language) # языки персонажа
    feats_pool = models.IntegerField(default = 0) # количество черт доступных для выбора
    feats = models.ManyToManyField(Feat) # черты персонажа

    def get_ability(self, tag):
        """Получение характеристики персонажа"""
        ability_value =  self.abilityvalues.get(ability=tag)
        return ability_value

    def go_to_level(self, level, class_id):
        """Обработка перехода на указанный уровень"""
        race_rules = self.race.rulesactingoncharlevelup.filter(Q(level=level) | Q(level=0))
        theme_rules = self.theme.rulesactingoncharlevelup.filter(Q(level=level) | Q(level=0))
        subrace_rules = []
        if self.subrace is not None:
            subrace_rules = self.subrace.rulesactingoncharlevelup.filter(Q(level=level) | Q(level=0))
        character_game_class = self.gameclasses.get(game_class_id = class_id)
        class_rules = character_game_class.game_class.rulesactingoncharlevelup.filter(Q(level=level) | Q(level=0))

        rules = list(chain(race_rules, theme_rules, class_rules, subrace_rules))        

        for rule in rules:
            if rule.operation == OperationChoice.Add.name:
                if rule.ability is not None:               
                    self.add_ability_value(rule.ability, rule.change_to)
                elif rule.skill is not None:
                    self.add_skill_value(rule.skill, rule.change_to)
                elif rule.character_property is not None:
                    self.__dict__[rule.character_property] += rule.change_to
            elif rule.operation == OperationChoice.Set.name:
                if rule.ability is not None:               
                    self.set_ability_value(rule.ability, rule.change_to)
                elif rule.skill is not None:
                    self.set_skill_value(rule.skill, rule.change_to)
                elif rule.character_property is not None:
                    self.__dict__[rule.character_property] = rule.change_to

        int_ability = self.get_ability(AbilityChoice.INT.name)
        self.skill_points_pool += int_ability.get_modifier()

        con_ability = self.get_ability(AbilityChoice.CON.name)
        self.stamina_points += con_ability.get_modifier()
        self.save()

    def add_ability_value(self, ability, value):
        """Прибавить значение к характеристике"""
        ability_value = self.get_ability(ability)
        ability_value.value += value
        ability_value.save()        

    def set_ability_value(self, ability, value):
        """Задать значение характеристики"""
        ability_value = self.get_ability(ability)
        ability_value.value = value
        ability_value.save()        

    def add_skill_value(self, skill, value):
        """Прибавить значение к навыку"""
        character_skill = self.skillvalues.get(skill=skill)
        character_skill.skill_points += value
        character_skill.save()        

    def set_skill_value(self, skill, value):
        """Задать значение навыка"""
        character_skill = self.skillvalues.get(skill=skill)
        character_skill.skill_points = value
        character_skill.save()      
 
    def add_distributed_skill_points(self, value):        
            self.distributed_skill_points += value

    def on_change_ability_value(self, ability_value):
        if ability_value.ability == AbilityChoice.CON.name:
            self.on_change_ability_constitution(ability_value)
        elif ability_value.ability == AbilityChoice.INT.name:
            self.on_change_ability_intelligence(ability_value)
    
    def on_change_ability_constitution(self, ability_value):
        modifier = ability_value.get_modifier()
        calculated_stamina_points = 0
        for char_game_class in self.gameclasses.all():
            calculated_stamina_points += (char_game_class.game_class.stamina_point_on_level + modifier) * char_game_class.level

        if self.stamina_points != calculated_stamina_points:
            self.stamina_points = calculated_stamina_points
            self.save()   

    def on_change_ability_intelligence(self, ability_value):
        modifier = ability_value.get_modifier()
        calculated_int_points = 0
        for char_game_class in self.gameclasses.all():
            calculated_int_points += (char_game_class.game_class.skill_point_on_level + modifier) * char_game_class.level

        # считаем сколько должно быть на уровне очков навыков вычитаем оттуда очки навыков в пуле навыков и распределенные очки навыков
        diff = calculated_int_points - self.skill_points_pool - self.distributed_skill_points 

        if diff != 0:
            self.skill_points_pool += diff
            self.save()


class CharacterGameClass(models.Model):  
    """Класс персонажа"""
    class Meta:
        unique_together = (("character", "game_class"),)  
    character = models.ForeignKey('Character',  related_name='gameclasses', on_delete=models.CASCADE) # персонаж
    game_class = models.ForeignKey('GameClass', on_delete=models.PROTECT) # игровой класс
    level = models.IntegerField() # уровень в классе персонажа


class CharacterSkillValue(models.Model):    
    """Значение навыка"""
    class Meta:
        unique_together = (("character", "skill"),)  
    character = models.ForeignKey('Character',  related_name='skillvalues', on_delete=models.CASCADE) # персонаж
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT) # навык
    skill_learned = models.BooleanField() # признак изученности навыка
    additional_info = models.CharField(max_length =255, null=True, blank=True) # дополнительная информация (например указание конкретной профессии)
    skill_points = models.IntegerField() # пункты вложенные в навык
    class_skill = models.BooleanField(default=False) # признак классового навыка


class AbilityValue(models.Model):
    """Значение характеристики"""
    class Meta:
        unique_together = (("character", "ability"),)

    ability = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in AbilityChoice], null=False)  # характеристика  
    character = models.ForeignKey('Character',  related_name='abilityvalues', on_delete=models.CASCADE) # персонаж
    value = models.IntegerField() # значение характеристики
    temp_value = models.IntegerField() # временное значение характеристики

    def get_modifier(self):
        return self.value//2 - 5

    def get_temp_modifier(self):
        return self.temp_value//2 - 5


    