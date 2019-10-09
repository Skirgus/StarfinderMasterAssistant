from django.db import models
from .choices import ArmorDamageTypeChoice, DiceTypeChoice, ArmorType

class BaseEquipment(models.Model):
    """Базовый класс для снаряжения"""
    
    name = models.CharField(max_length=255) # название снаряжения
    description = models.TextField(null=True, blank=True) # описание снаряжения
    level = models.IntegerField() # уровень снаряжения
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # стоимость снаряжения
    bulk = models.DecimalField(max_digits=5, decimal_places=2) # вес снаряжения
    image = models.ImageField(upload_to='equipment/', null=True, blank=True) # миниатюра для списка

class WeaponCategory(models.Model):
    """Категория оружия"""
    name = models.CharField(max_length=255) # название категории
    description = models.TextField(null=True, blank=True)  # описание
    armor_damage_type = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in ArmorDamageTypeChoice])  # тип брони, блокирующий урон

class WeaponType(models.Model):
    """Тип оружия"""
    name = models.CharField(max_length=255) # название типа оружия
    description = models.TextField(null=True, blank=True)  # описание

class CriticalEffect(models.Model):
    """Тип критического удара"""
    name = models.CharField(max_length=255) # название крита
    description = models.TextField(null=True, blank=True)  # описание

class WeaponSpecial(models.Model):
    """Особые свойства оружия"""
    name = models.CharField(max_length=255) # название 
    description = models.TextField(null=True, blank=True)  # описание

class Weapon(BaseEquipment):
    """Базовый класс для оружия"""
    count_hand = models.IntegerField() # количество рук
    damage_dice_count = models.IntegerField(null=True, blank=True) # количество бросков кубика
    damage_dice_type = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in DiceTypeChoice])  # количество граней кубика
    critical_effect = models.ForeignKey('CriticalEffect', on_delete=models.PROTECT, null=True, blank=True) # тип критического удара
    critical_dice_count = models.IntegerField(null=True, blank=True) # количество бросков кубика
    critical_dice_type = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in DiceTypeChoice],null=True, blank=True)  # количество граней кубика                         
    category = models.ForeignKey('WeaponCategory', on_delete=models.PROTECT) # категория оружия
    weapon_type = models.ForeignKey('WeaponType', on_delete=models.PROTECT) # тип оружия
    special = models.ManyToManyField(WeaponSpecial) # особые свойства оружия

class Armor(BaseEquipment):
    """Базовый класс для брони"""
    type_armor = models.CharField(max_length=255, 
                            choices=[(tag.name, tag.value) 
                            for tag in ArmorType],null=False, blank=True)  # тип брони
    eac = models.IntegerField() # ЭКБ броня
    kac = models.IntegerField() # ККБ броня
    armor_check_penalty = models.IntegerField() #  штраф за ношение брони 
    speed_adjustment = models.IntegerField() # скорость
    upgrade_slots = models.IntegerField() # количество слотов под улучшения
    max_dex = models.IntegerField() # максимальная ловкость

