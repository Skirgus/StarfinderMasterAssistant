from .models import Character

class CharacterBuilder():    
    """
    Строитель персонажа
    """
    BASE_ABILITY_POOL = 10

    def __init__(self) -> None:
        """
        Новый экземпляр строителя должен содержать пустой объект персонажа,
        который используется в дальнейшей сборке.
        """
        self.reset()

    def reset(self) -> None:
        self._character = Character()

    def character(self, name, race_id, theme_id, alignment_id, deity_id, class_id, gender) -> Character:        
        character = self._character



        self.reset()
        return character

    def set_base_fields(self, name, alignment_id, deity_id, gender, race_id, theme_id):
        character = self.character
        character.name = name
        character.gender = gender
        character.ability_pool = BASE_ABILITY_POOL
        


