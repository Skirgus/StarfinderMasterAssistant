from .dto import AbilityValueBlankDto, CharacterClassBlankDto, SkillValueBlankDto, CharacterBlankDto
from .choices import AbilityChoice

class CharacterManager():
    """
    Предоставляет методы для работы с персонажем
    """
    def __init__(self, character):
        self.character = character

    def get_ability_values(self):
        """
        Получение списка dto характеристик
        """
        ability_value_dtos = []
        
        for ability_value in self.character.abilityvalues.all():
            ability_title = AbilityChoice[ability_value.ability].value
            dto = AbilityValueBlankDto(ability_title, ability_value.value, ability_value.get_modifier(),
                ability_value.temp_value, ability_value.get_temp_modifier())
            ability_value_dtos.append(dto)
        
        return ability_value_dtos
    
    def get_character_classes(self):
        """
        Получение списка dto классов персонажа
        """
        character_classes = []

        for character_class in self.character.gameclasses.all():
            dto = CharacterClassBlankDto(character_class.game_class.name, character_class.level)
            character_classes.append(dto)
        
        return character_classes

    def get_other_skill_modifier(self, skill):
        """
        Получение прочих модификаторов навыка
        """
        #todo заглушка, в дальнейшем тут надо описанть получение прочих модификаторов навыковы
        return 0

    def get_initiative_modifier(self):
        """
        Получение модификатров инициативы
        """
        #todo заглушка, в дальгейшем тут надо описанть получение прочих модификаторов инициативы
        return 0

    def get_skill_values(self):
        """
        Получение списка dto навыков
        """
        skill_values = []

        for skill_value in self.character.skillvalues.all():
            name = skill_value.skill.name + '(' + AbilityChoice[skill_value.skill.ability].value + ')'
            class_points = 3 if skill_value.class_skill else 0
            ability_modifier = self.character.get_ability(skill_value.skill.ability).get_modifier()
            other_modifier= self.get_other_skill_modifier(skill_value)
            dto = SkillValueBlankDto(name, skill_value.skill_points, class_points, ability_modifier, other_modifier)
            skill_values.append(dto)
        return skill_values

    def get_blank_dto(self):
        """
        Получение dto персонажа, для распечатки бланка персонажа
        """
        abilities = self.get_ability_values()
        classes = self.get_character_classes()
        skills = self.get_skill_values()
        initiative_modifier = self.get_initiative_modifier()
        return CharacterBlankDto(self.character, initiative_modifier, classes, abilities, skills)

