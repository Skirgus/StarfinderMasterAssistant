from rest_framework import serializers
from .models import Race, RaceDescription, RacePlayingFor

class RaceDescriptionSerializer(serializers.ModelSerializer):
     class Meta:
        model = RaceDescription
        fields = ('title', 'text')


class RacePlayingForSerializer(serializers.ModelSerializer):
     class Meta:
        model = RacePlayingFor
        fields = ('title', 'text')


class RaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('id', 'name', 'title_info', 'title_image')


class RaceSerializer(serializers.ModelSerializer):
    descriptions = RaceDescriptionSerializer(many=True, read_only=True)
    playingforinformations = RacePlayingForSerializer(many=True, read_only=True)
    class Meta:
        model = Race
        fields = ('id', 'name', 'basic_info', 'basic_image', 'min_average_weight', 'max_average_weight',
         'min_average_height', 'max_average_height', 'age_of_majority', 'descriptions', 'playingforinformations')