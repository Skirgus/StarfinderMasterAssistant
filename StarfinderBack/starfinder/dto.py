from .choices import SexChoice, AbilityChoice

class RaceListDto:
    """
    Dto для списка рас

        id - идентификатор
        displayName - отображаемое название

    """
    def __init__(self, id, displayName):
        self.id = id
        self.displayName = displayName

class AbilityValueBlankDto:
    """
    Dto для значения зхарактеристики
    """    
    def __init__(self, title, value, modifier, temp_value, temp_modifier):
        self.title = title
        self.value = value
        self.modifier = modifier
        self.temp_value = temp_value
        self.temp_modifier = temp_modifier

class SkillValueBlankDto:
    """
    Dto для значения зхарактеристики
    """    
    def __init__(self, title, skill_points, class_point, ability_modifier, other_modifier):
        self.title = title
        self.skill_points = skill_points
        self.class_points = class_point
        self.ability_modifier = ability_modifier
        self.other_modifier = other_modifier
        self.total = self.skill_points + self.class_points + self.ability_modifier + self.other_modifier

class CharacterClassBlankDto:
    """
    Dto для класса персонажа
    """    
    def __init__(self, name, level):
        self.name = name
        self.level = level

#todo должен ли dto знать как должны вычисляться общая инициатива и т.д.
#скорее всего нет, но вычислять где то снаружи тоже так себе вариант(
#пусть будет пока тут
class CharacterBlankDto:
    """
    Dto персонажа для бланка
    """    
    def __init__(self, character, initiative_modifiers, character_classes, ability_values, skill_values):
        self.username = character.user.username #имя игрока
        self.name = character.name # имя персонажа        
        self.gender = SexChoice[character.gender].value # пол
        self.description = character.description # описание
        self.race = character.race.name # раса
        self.theme = character.theme.name # тема
        self.alignment = character.alignment.name # мировозрение
        self.deity = character.deity.name if character.deity is not None else '' # божество
        self.skill_points_pool = character.skill_points_pool # очки навыков доступные для распределения
        self.level = character.level # уровень
        self.basic_attack_bonus = character.basic_attack_bonus # базовый модификатор атаки
        self.basic_fortitude = character.basic_fortitude # базовая стойкость
        self.basic_reflex = character.basic_reflex # базовая реакция
        self.basic_will = character.basic_will # базовая воля
        self.hit_points = character.hit_points # пункты здоровья
        self.stamina_points = character.stamina_points # пункты живучести
        self.resolve_points = character.resolve_points # пункты решимости 
        self.initiative_modifiers = initiative_modifiers # прочие модификаторы инициативы
        self.total_initiative = character.get_ability(AbilityChoice.DEX.name).get_modifier() + self.initiative_modifiers #инициатива
        self.dex_modifier = character.get_ability(AbilityChoice.DEX.name).get_modifier() # модификатор ловкости
        self.character_classes = character_classes #классы персонажа
        self.ability_values = ability_values #характеристики
        self.skill_values = skill_values #навыки