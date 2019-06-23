from rest_framework import serializers

class RaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    min_average_weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    max_average_weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    min_average_height = serializers.DecimalField(max_digits=5, decimal_places=2)
    max_average_height = serializers.DecimalField(max_digits=5, decimal_places=2)
    age_of_majority = serializers.IntegerField()
    basic_info = serializers.CharField()
    title_info = serializers.CharField()
    basic_image = serializers.ImageField()
    title_image = serializers.ImageField()


class RaceDescriptionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    race_id = serializers.IntegerField()


class RacePlayingForSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    race_id = serializers.IntegerField()