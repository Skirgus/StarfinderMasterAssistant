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
    feats_pool = "Количество черт доступных для выбора"
    experience_to_level_up = "Опыт для повышения уровня"

class ArmorDamageTypeChoice(Enum):
    """Тип урона по броне"""
    EAC = "ЭКБ"
    KAC = "ККБ"
    EAC_KAC = "ЭКБ & ККБ"

class DiceTypeChoice(Enum):
    """Тип кубика"""
    D3 = "d3"
    D4 = "d4"
    D6 = "d6"
    D8 = "d8"
    D10 = "d10"
    D12 = "d12"
    D20 = "d20"
    D100 = "d100"

class ArmorType(Enum):
    """Тип брони"""
    light = "Легкая броня"
    heavy = "Тяжелая броня"
