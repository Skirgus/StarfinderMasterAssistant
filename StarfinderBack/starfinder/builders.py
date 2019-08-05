import django
from .models import Character, Race, Alignment, Deity, Theme, GameClass
from .models import AbilityChoice, Skill, World


class CharacterBuilder():    
    """
    Строитель персонажа
    """
    BASE_ABILITY_POOL = 10
    BASE_ABILITY_VALUE = 10

    def __init__(self) -> None:
        """
        Новый экземпляр строителя должен содержать пустой объект персонажа,
        который используется в дальнейшей сборке.
        """
        self.reset()

    def reset(self) -> None:
        self._character = Character()

    def character(self, name, race_id, theme_id, alignment_id, deity_id, class_id, gender, user, world_id) -> Character:  
        try:      
            character = self._character
            self.set_base_fields(name, alignment_id, deity_id, gender, race_id, theme_id, user, world_id)
            self.set_class(class_id)
            self.create_character_abilities()
            self.create_character_skills()

            character.go_to_level(1, class_id)
            self.reset()
            return character
        except Exception:
            if character.id is not None:
                character.delete()
            raise Exception            

    def set_base_fields(self, name, alignment_id, deity_id, gender, race_id, theme_id, user, world_id):
        character = self._character
        character.name = name
        character.gender = gender
        character.ability_pool = self.BASE_ABILITY_POOL
        character.race = Race.objects.get(id=race_id)
        character.theme = Theme.objects.get(id=theme_id)
        character.alignment = Alignment.objects.get(id=alignment_id)
        character.level = 1
        if deity_id is not None:
            character.deity = Deity.objects.get(id=deity_id)
        if world_id is not None:
            character.home_world = World.objects.get(id=world_id)
        character.user = user
        character.save()
    
    def set_class(self, class_id):
        character = self._character
        game_class = GameClass.objects.get(id=class_id)
        character.gameclasses.create(game_class=game_class, level=1)
    
    def create_character_abilities(self):
        character = self._character
        for ability_choice in AbilityChoice:
            character.abilityvalues.create(ability=ability_choice.name,
                value=self.BASE_ABILITY_VALUE, temp_value=self.BASE_ABILITY_VALUE)

    def create_character_skills(self):
        character = self._character
        skill_array = Skill.objects.all()
        for skill in skill_array:
            character.skillvalues.create(skill=skill, skill_learned=False, skill_points=0)
