from django.db import models
from enum import Enum


class SexChoice(Enum):
    """Пол"""
    Male = "Мужской"
    Femail = "Женский"


class СharacteristicChoice(Enum):
    """Характеристика"""
    STR = "Сила"
    DEX = "Ловкость"
    CON = "Выносливость"
    Int = "Интеллект"
    WIS = "Мудрость"
    CHA = "Харизма"


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

class SubRace(models.Model):
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
    age_of_majority = models.IntegerField() # возраст совершеннолетия
    basic_info = models.TextField() # базовая информация
    title_info = models.TextField() # информация для списка
    basic_image = models.ImageField(upload_to='themes/', null=True, blank=True) # изображение
    title_image = models.ImageField(upload_to='themes/', null=True, blank=True) # миниатюра для списка
    base_characteristic = models.CharField(max_length=5, 
                            choices=[(tag, tag.value) 
                            for tag in СharacteristicChoice], null=True)  # базовая характеристика

    
class Character(model.Model): 
    """Персонаж""" 
    user = models.ForeignKey('User',  related_name='characters', on_delete=models.CASCADE)      
    name = models.CharField(max_length=255, unique=True, message="") # имя персонажа
    portrait = models.ImageField(upload_to='character_portraits/', null=True, blank=True) # портрет персонажа
    sex = models.CharField(max_length=5, choices=[(tag, tag.value) for tag in SexChoice])  # пол
    description = models.TextField() # описание
    race = models.ForeignKey('Race',  related_name='characters', on_delete=models.CASCADE) # раса
    сharacteristic_pool = models.IntegerField(default=0) # очки характеристик доступные для распределения


class CharacteristicValue(model.Model):
    """Значение характеристики"""
    character = models.ForeignKey('Character',  related_name='characteristicvalues', on_delete=models.CASCADE) # характеристика
    value = models.IntegerField() # значение характеристики
    temp_value = models.IntegerField() # временное значение характеристики

    def get_modifier(self):
        return value//2 - 5

    def get_temp_modifier(self):
        return temp_value//2 - 5