from django.db import models
from enum import Enum


class SexChoice(Enum):
    """Пол"""
    Male = "Мужской"
    Femail = "Женский"


class AbilityChoice(Enum):
    """Характеристика"""
    STR = "Сила"
    DEX = "Ловкость"
    CON = "Выносливость"
    Int = "Интеллект"
    WIS = "Мудрость"
    CHA = "Харизма"

class CharacterPropertiesChoice(Enum):
    """Свойства персонажа"""
    basic_attack_bonus = "Базовый модификатор атаки"
    basic_fortitude = "Базовая стойкость"
    basic_reflex = "Базовая реакция"
    basic_will = "Базовая воля"
    hit_points = "Пункты здоровья"
    stamina_points = "Пункты живучести"
    resolve_points = "Пункты решимости"
    ability_pool = "Очки характеристик доступные для распределения"
    skill_points_pool = "Очки навыков доступные для распределения"


# Create your models here.
class Race(models.Model):
    """Раса"""
    name = models.CharField(max_length=255) # название расы
    min_average_weight = models.DecimalField(max_digits=5, decimal_places=2) # средний вес, нижняя граница
    max_average_weight = models.DecimalField(max_digits=5, decimal_places=2) # средний вес, верхняя граница
    min_average_height = models.DecimalField(max_digits=5, decimal_places=2) # средний рост, нижняя граница
    max_average_height = models.DecimalField(max_digits=5, decimal_places=2) # средний рост, нижняя граница
    age_of_majority = models.IntegerField() # возраст совершеннолетия
    basic_info = models.TextField() # базовая информация
    title_info = models.TextField() # информация для списка
    basic_image = models.ImageField(upload_to='races/', null=True, blank=True) # изображение
    title_image = models.ImageField(upload_to='races/', null=True, blank=True) # миниатюра для списка
    
    def __str__(self):
        return self.name


class Alignment(models.Model):
    """Мировозрение"""
    class Meta:
        unique_together = (("lawfull_chaotic", "good_evil"),)

    LAWFULL = 0
    NEUTRAL = 1
    CHAOTIC = 2
    LAWFULL_CHAOTIC_CHOICES = (
        (LAWFULL, 'Принципиальный'),
        (NEUTRAL, 'Нейтральный'),
        (CHAOTIC, 'Хаотичный')
    )

    GOOD = 0
    EVIL = 2
    GOOD_EVIL_CHOICES =(
        (GOOD, 'Добрый'),
        (NEUTRAL, 'Нейтральный'),
        (EVIL, 'Злой')
    )    

    lawfull_chaotic = models.IntegerField(choices=LAWFULL_CHAOTIC_CHOICES, default=NEUTRAL) # принципиальный-хаотичный
    good_evil = models.IntegerField(choices=GOOD_EVIL_CHOICES, default=NEUTRAL) # добрый-злой
    name = models.CharField(max_length =255) # название подрасы
    description = models.TextField() # описание

    def __str__(self):
        return self.name

class Deity(models.Model):
    """Божество"""
    name = models.CharField(max_length =255) # имя
    alignment = models.ForeignKey('Alignment', on_delete=models.PROTECT) # мировозрение
    portfolios = models.CharField(max_length =255) # область интересов
    description = models.TextField()
    symbol = models.ImageField(upload_to='deities/', null=True, blank=True) # изображение


class Subrace(models.Model):
    """Подраса"""
    name = models.CharField(max_length =255) # название подрасы
    description = models.TextField() # информация
    race = models.ForeignKey('Race',  related_name='subraces', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.race.name + ' '+ self.name


class RaceDescription(models.Model):
    """Описание расы"""
    title = models.CharField(max_length=255) # заголовок
    text = models.TextField() # описание
    race = models.ForeignKey('Race',  related_name='descriptions', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '(' + self.race.name + ')'


class RacePlayingFor(models.Model):
    """Информация для отыгрыша расы"""
    YOUR_MOST_LIKELY = 'YOUR'
    OTHER_RACES_MOST_LIKELY = 'OTHER'
    PLAYING_FOR_CHOICES = (
        (YOUR_MOST_LIKELY, 'Вы скорее всего...'),
        (OTHER_RACES_MOST_LIKELY, 'Другие расы скорее всего...')
    )
    title = models.CharField(max_length=255,choices=PLAYING_FOR_CHOICES, default=YOUR_MOST_LIKELY) # заголовок
    text = models.TextField() # описание
    race = models.ForeignKey('Race',  related_name='playingforinformations', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text + '(' + self.race.name + ')'


class Theme(models.Model):
    """Тема"""
    name = models.CharField(max_length=255) # название темы
    basic_info = models.TextField() # базовая информация
    title_info = models.TextField() # информация для списка
    basic_image = models.ImageField(upload_to='themes/', null=True, blank=True) # изображение
    title_image = models.ImageField(upload_to='themes/', null=True, blank=True) # миниатюра для списка
    base_ability = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in AbilityChoice], null=True, blank=True)  # базовая характеристика
                          
    def __str__(self):
        return self.name


class GameClass(models.Model):
    """Класс"""
    name = models.CharField(max_length=255) # название класса
    basic_info = models.TextField() # базовая информация
    title_info = models.TextField() # информация для списка
    basic_image = models.ImageField(upload_to='classes/', null=True, blank=True) # изображение
    title_image = models.ImageField(upload_to='classes/', null=True, blank=True) # миниатюра для списка
    main_ability = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in AbilityChoice])  # основная характеристика
    hit_points_on_level = models.IntegerField() # пункты здоровья за уровень
    stamina_point_on_level = models.IntegerField() # пункты живучести за уровень (прибавляются вместе с модификатором выносливости)
    skill_point_on_level = models.IntegerField()  # пункты навыков за уровень (прибавляются вместе с модификатором интелекта)     
    
    def __str__(self):
        return self.name                 


class Skill(models.Model):
    """Навык"""
    name = models.CharField(max_length=255) # название
    ability = models.CharField(max_length=5, 
                            choices=[(tag.name, tag.value) 
                            for tag in AbilityChoice], null=True)  # основная характеристика
    without_learning = models.BooleanField(default=True) # можно повышать без изучения
    armor_penalty_applies = models.BooleanField(default=False) # применяется штраф на броню
    description = models.TextField() # описание
    need_additional_info = models.BooleanField(default=False) # необходима дополнительная информация


class Character(models.Model): 
    """Персонаж""" 
    user = models.ForeignKey('auth.User',  related_name='characters', on_delete=models.CASCADE)      
    name = models.CharField(max_length=255, unique=True) # имя персонажа
    portrait = models.ImageField(upload_to='character_portraits/', null=True, blank=True) # портрет персонажа
    sex = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in SexChoice])  # пол
    description = models.TextField() # описание
    race = models.ForeignKey('Race',  related_name='characters', on_delete=models.CASCADE) # раса
    theme = models.ForeignKey('Theme',  related_name='characters', on_delete=models.CASCADE) # тема
    alignment = models.ForeignKey('Alignment', on_delete=models.PROTECT) # мировозрение
    deity = models.ForeignKey('Deity', null=True, blank=True, on_delete=models.SET_NULL) # божество
    ability_pool = models.IntegerField(default=0) # очки характеристик доступные для распределения
    skill_points_pool = models.IntegerField(default=0) # очки навыков доступные для распределения
    level = models.IntegerField() # уровень
    basic_attack_bonus = models.IntegerField() # базовый модификатор атаки
    basic_fortitude = models.IntegerField() # базовая стойкость
    basic_reflex = models.IntegerField() # базовая реакция
    basic_will = models.IntegerField() # базовая воля
    hit_points = models.IntegerField() # пункты здоровья
    stamina_points = models.IntegerField() # пункты живучести
    resolve_points = models.IntegerField() # пункты решимости 

    def get_ability(self, tag):
        ability_value = (ability_value for ability_value in self.abilityvalues if ability_value.ability == tag)
        return ability_value


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
    additional_info = models.CharField(max_length =255) # дополнительная информация (например указание конкретной профессии)
    skill_points = models.IntegerField() # пункты вложенные в навыкs


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
        return value//2 - 5

    def get_temp_modifier(self):
        return temp_value//2 - 5


class BaseRule(models.Model):
    """Базовый класс для правил"""
    class Meta:
        abstract = True
    name = models.CharField(max_length=255, null=True, blank=True) # название правила
    description = models.CharField(max_length=255, null=True, blank=True) # описание правила


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


class RaceRulesActingOnCharLevelUp(RulesActingOnCharLevelUp):
    """Правила расы действующие при повышении в уровне"""
    race = models.ForeignKey('Race',  related_name='rulesactingoncharlevelup', on_delete=models.CASCADE) # раса

    
class ThemeRulesActingOnCharLevelUp(RulesActingOnCharLevelUp):
    """Правила темы действующие при повышении в уровне"""
    theme = models.ForeignKey('Theme',  related_name='rulesactingoncharlevelup', on_delete=models.CASCADE) # тема
    
    
class ClassRulesActingOnCharLevelUp(RulesActingOnCharLevelUp):
    """Правила класса действующие при повышении в уровне"""
    game_class = models.ForeignKey('GameClass',  related_name='rulesactingoncharlevelup', on_delete=models.CASCADE) # тема