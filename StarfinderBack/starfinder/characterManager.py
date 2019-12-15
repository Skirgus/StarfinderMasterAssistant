from .dto import AbilityValueBlankDto, CharacterClassBlankDto, SkillValueBlankDto, CharacterBlankDto
from .choices import AbilityChoice, OperationChoice
from .feat import Feat, RuleChoice, PrerequestUnionChoice
from .models import GameClass
from .ruleModels import GeneralRulesOnCharLevelUp
from .character import CharacterGameClass
from django.db.models import Q
from itertools import chain

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

    
    def level_up(self, game_class_id):
        """
        Повышение уровня персонажа
        """    
        if not self.character.level_up_available:
            raise ValueError("Повышение уровня не доступно")

        self.character.level += 1
        self._set_class(game_class_id)
        self._handle_level_up(game_class_id)


    def _handle_level_up(self, class_id):
        """Обработка перехода на указанный уровень"""
        character = self.character
        level = character.level
        general_rules = GeneralRulesOnCharLevelUp.objects.filter(Q(level=level) | Q(level=0))
        race_rules = character.race.rulesactingoncharlevelup.filter(Q(level=level) | Q(level=0))
        theme_rules = character.theme.rulesactingoncharlevelup.filter(Q(level=level) | Q(level=0))
        subrace_rules = []
        if character.subrace is not None:
            subrace_rules = character.subrace.rulesactingoncharlevelup.filter(Q(level=level) | Q(level=0))
        character_game_class = character.gameclasses.get(game_class_id = class_id)
        class_rules = character_game_class.game_class.rulesactingoncharlevelup.filter(Q(level=character_game_class.level) | Q(level=0))

        rules = list(chain(general_rules, race_rules, theme_rules, class_rules, subrace_rules))        

        for rule in rules:
            if rule.operation == OperationChoice.Add.name:
                if rule.ability is not None:               
                    character.add_ability_value(rule.ability, rule.change_to)
                elif rule.skill is not None:
                    character.add_skill_value(rule.skill, rule.change_to)
                elif rule.character_property is not None:
                    character.__dict__[rule.character_property] += rule.change_to
            elif rule.operation == OperationChoice.Set.name:
                if rule.ability is not None:               
                    character.set_ability_value(rule.ability, rule.change_to)
                elif rule.skill is not None:
                    character.set_skill_value(rule.skill, rule.change_to)
                elif rule.character_property is not None:
                    character.__dict__[rule.character_property] = rule.change_to

        int_ability = character.get_ability(AbilityChoice.INT.name)
        character.skill_points_pool += int_ability.get_modifier()

        con_ability = character.get_ability(AbilityChoice.CON.name)
        character.stamina_points += con_ability.get_modifier()
        character.save()

    
    def _set_class(self, class_id):
        """
        Задает класс при повышении уровня
        """
        character = self.character
        try:
            character_game_class = character.gameclasses.get(game_class_id = class_id)
            character_game_class.level += 1
            character_game_class.save()
        except CharacterGameClass.DoesNotExist:
            game_class = GameClass.objects.get(id=class_id)
            character.gameclasses.create(game_class=game_class, level=1)
            self._set_class_skills(class_id)


    def _set_class_skills(self, class_id):
        """
        Устанавливает классовые способности персонажа
        """
        character = self.character
        theme_rules = character.theme.set_class_skill_rules.all()

        character_game_class = character.gameclasses.get(game_class_id = class_id)
        class_rules = character_game_class.game_class.set_class_skill_rules.all()
                
        rules = list(chain(theme_rules, class_rules)) 

        for rule in rules:
            rule_skill = rule.skill
            character_skill = character.skillvalues.get(skill=rule_skill)
            if character_skill.class_skill:
                character_skill.skill_points += 1
            else: 
                character_skill.class_skill = True
            character_skill.save()


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

    
    def get_feats_by_character(self):
        """Получение черт доступных для выбора персонажем"""
        feats_queryset = Feat.objects.all()
        feat_by_choice = []
        character_feats = self.character.feats.all()
        for feat in feats_queryset:
            if self.validate_feat(feat):
                feat_by_choice.append(feat)
        return feat_by_choice


    def validate_feat(self, feat):
        """Проверка, удовлетворяет ли персонаж условиям черты"""        
        character_feat = self.character.feats.filter(id=feat.id).count()
        if character_feat > 0:
            return False

        prerequests = feat.prerequests.all()  
        if len(prerequests) == 0:
            return True
        
        prerequest_handle_result = None
        for prerequest in prerequests:
            prerequest_handle_result = self._handle_feat_prerequest(prerequest, prerequest_handle_result)
        return prerequest_handle_result


    def _handle_feat_prerequest(self, prerequest, prev_prerequest_result = None):
        """Обработка условия черты"""        
        if prerequest.ability is not None:
            prerequest_match = self._check_ability(prerequest)
        elif prerequest.skill is not None:
            prerequest_match = self._check_skills(prerequest)
        elif prerequest.character_property is not None:
            prerequest_match = self._check_property(prerequest) 
        elif prerequest.required_feat is not None:
            prerequest_match  = self._check_character_feats(prerequest)

        if prev_prerequest_result is None:
            return prerequest_match
        elif prerequest.union_rule == PrerequestUnionChoice.And.name:
            return prerequest_match and prev_prerequest_result
        else:
            return prerequest_match or prev_prerequest_result


    def _check_ability(self, prerequest):
        """Проверка характеристики"""
        character_ability_value = self.character.get_ability(prerequest.ability).value
        if prerequest.rule == RuleChoice.at_least.name:
            return character_ability_value >= prerequest.value
        elif prerequest.rule == RuleChoice.less.name:
            return character_ability_value < prerequest.value
        else:
             raise ValueError("Не коррректно составлено предусловие " + prerequest.feat.name + "-" + prerequest.description + ". " +
             "Для предусловий характеристик должны быть выбраны правила или 'Не менее' или 'Меньше'")


    def _check_skills(self, prerequest):
        """Проверка навыков"""
        skill_value = self.character.skillvalues.get(skill=prerequest.skill).skill_points
        if prerequest.rule == RuleChoice.at_least.name:
                return skill_value >= prerequest.value
        elif prerequest.rule == RuleChoice.less.name:
            return skill_value < prerequest.value
        elif prerequest.rule == RuleChoice.must_be.name:
            return (skill_value is None or skill_value > 0)
        else:
            return skill_value is None or skill_value <= 0


    def _check_property(self, prerequest):
        """Проверка свойств персонажа"""
        property_value =  self.character.__dict__[prerequest.character_property]
        if prerequest.rule == RuleChoice.at_least.name:
                return property_value >= prerequest.value
        elif prerequest.rule == RuleChoice.less.name:
            return property_value < prerequest.value
        else:
             raise ValueError("Не коррректно составлено предусловие " + prerequest.feat.name + "-" + prerequest.description + ". " +
             "Для предусловий свойств персонажа должны быть выбраны правила или 'Не менее' или 'Меньше'")        


    def _check_character_feats(self, prerequest):
        """Проверка существующих черт персонажа"""        
        feat = self.character.feats.filter(id=prerequest.required_feat.id).count()
        if prerequest.rule == RuleChoice.must_be.name:            
            return feat > 0
        elif prerequest.rule == RuleChoice.must_be_absent.name:
            return feat == 0
        else:
            raise ValueError("Не коррректно составлено предусловие " + prerequest.feat.name + "-" + prerequest.description + ". " +
             "Для предусловий черт должны быть выбраны правила или 'Должны быть' или 'Должны отсутствовать'")       