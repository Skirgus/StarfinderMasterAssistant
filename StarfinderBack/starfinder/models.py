from django.db import models
from django.db.models import Q
from itertools import chain
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, get_list_or_404
from .choices import AbilityChoice, SexChoice, OperationChoice, CharacterPropertiesChoice

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
    language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, blank=True) # язык
    title_info = models.TextField() # информация для списка
    basic_image = models.ImageField(upload_to='races/', null=True, blank=True) # изображение
    title_image = models.ImageField(upload_to='races/', null=True, blank=True) # миниатюра для списка
    
    def __str__(self):
        return self.name


class Language(models.Model):
    """Язык"""
    name = models.CharField(max_length=255) # название языка

    def __str__(self):
        return self.name


class World(models.Model):
    """Мир"""
    NONE = 0
    THIN = 1
    NORMAL = 2
    SPECIAL = 3
    TOXIC_AND_THIN = 4
    NORMAL_OR_NONE = 5
    TOXIC = 6
    AIR_CHOISE = (
        (NONE, 'Отсутствует'),
        (THIN, 'Разряжённая'),
        (NORMAL, 'Обычная'),
        (SPECIAL, 'Особая'),
        (TOXIC_AND_THIN, 'Токсичная и разряжённая'),
        (NORMAL_OR_NONE, 'Обычная или отсутствует'),
        (TOXIC, 'Токсичная')
    )

    name = models.CharField(max_length=255) # наименование планеты
    byname = models.CharField(max_length=255, null=True, blank=True) # прозвание планеты
    diam = models.CharField(max_length=255) # диаметр планеты
    weight = models.CharField(max_length=255) # масса 
    gravity = models.CharField(max_length=255) # гравитация
    air = models.IntegerField(choices=AIR_CHOISE, default=NORMAL) # атмосфера
    day = models.CharField(max_length=255, null=True, blank=True) # день
    year = models.CharField(max_length=255, null=True, blank=True) # год
    described = models.TextField() # описание планеты
    planet_image = models.ImageField(upload_to='world/', null=True, blank=True) # изображение планеты
    panoramic_image = models.ImageField(upload_to='world/', null=True, blank=True) # панорама пейзажа
    language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, blank=True) # язык

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
    
    def __str__(self):
        return self.name 


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
    
    def __str__(self):
        return self.name 