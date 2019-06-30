from rest_framework import serializers
from .models import Race, RaceDescription, RacePlayingFor, Subrace
from .models import Theme, GameClass

class RaceDescriptionSerializer(serializers.ModelSerializer):
     class Meta:
        model = RaceDescription
        fields = ('title', 'text')


class RacePlayingForSerializer(serializers.ModelSerializer):
     class Meta:
        model = RacePlayingFor
        fields = ('title', 'text')

class SubraceSerializer(serializers.ModelSerializer):
     class Meta:
        model = Subrace
        fields = ('name', 'description')


class RaceListSerializer(serializers.ModelSerializer):
    subraces = SubraceSerializer(many=True, read_only=True)
    class Meta:
        model = Race
        fields = ('id', 'name', 'title_info', 'title_image', 'subraces')


class RaceSerializer(serializers.ModelSerializer):
    descriptions = RaceDescriptionSerializer(many=True, read_only=True)
    playingforinformations = RacePlayingForSerializer(many=True, read_only=True)
    subraces = SubraceSerializer(many=True, read_only=True)
    class Meta:
        model = Race
        fields = ('id', 'name', 'basic_info', 'basic_image', 'min_average_weight', 'max_average_weight',
         'min_average_height', 'max_average_height', 'age_of_majority', 'descriptions', 'playingforinformations', 'subraces')


class ThemeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'name', 'title_info', 'title_image')


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'name', 'basic_info', 'basic_image', 'base_ability')

        
class GameClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameClass
        fields = ('id', 'name', 'title_info', 'title_image')


class GameClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameClass
        fields = ('id', 'name', 'basic_info', 'basic_image', 'main_ability', 'hit_points_on_level', 'stamina_point_on_level', 'skill_point_on_level')

        
class CharacterListSerializer(serializers.ModelSerializer):
    race = serializers.CharField(read_only=True, source="race.name")
    theme = serializers.CharField(read_only=True, source="theme.name")
    class Meta:
        model = Theme
        fields = ('id', 'name', 'description', 'portrait', 'race', 'theme')