from enum import Enum


class SexChoice(Enum):
    """Пол"""
    Male = "Мужской"
    Femail = "Женский"

    
class OperationChoice(Enum):
    """Операция"""
    Add = "Прибавить"
    Set = "Установить"


class AbilityChoice(Enum):
    """Характеристика"""
    STR = "Сила"
    DEX = "Ловкость"
    CON = "Выносливость"
    INT = "Интеллект"
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