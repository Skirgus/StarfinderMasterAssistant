# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Race, RaceDescription, RacePlayingFor
from .models import Theme, GameClass, Character, Deity, World, Language
from .serializers import RaceSerializer, RaceDescriptionSerializer, RacePlayingForSerializer, RaceListSerializer, DeitySerializer, LanguageSerializer
from .serializers import ThemeListSerializer, ThemeSerializer, GameClassListSerializer, GameClassSerializer, CharacterListSerializer, CharacterSerializer
from .serializers import WorldSerializer, WorldListSerializer, WeaponSerializer, ArmorSerializer
from .builders import CharacterBuilder
from .dto import AbilityValueBlankDto
from .characterManager import CharacterManager
from .equipment import Weapon, Armor
from .feat import Feat, FeatListSerializer
import json

# Create your views here.

class RacesView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка рас
        """
        races = Race.objects.all()                
        serializer = RaceListSerializer(races, many=True)
        return Response({"races": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение расы по идентификатору

        pk - идентификатор расы
        """
        queryset = Race.objects.all()
        race = get_object_or_404(queryset, pk=pk)
        serializer = RaceSerializer(race)        
        return Response(serializer.data)

class WeaponView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка оружия
        """
        weapons = Weapon.objects.all()                
        serializer = WeaponSerializer(weapons, many=True)
        return Response({"Weapons": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение оружия по идентификатору

        pk - идентификатор оружия
        """
        queryset = Weapon.objects.all()
        weapon = get_object_or_404(queryset, pk=pk)
        serializer = WeaponSerializer(weapon)        
        return Response(serializer.data)

class ArmorView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка брони
        """
        armors = Armor.objects.all()                
        serializer = ArmorSerializer(armors, many=True)
        return Response({"Armors": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение брони по идентификатору

        pk - идентификатор брони
        """
        queryset = Armor.objects.all()
        armor = get_object_or_404(queryset, pk=pk)
        serializer = ArmorSerializer(armor)        
        return Response(serializer.data)

class WorldsView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка миров
        """
        worlds = World.objects.all()
        serializer = WorldListSerializer(worlds, many=True)
        return Response({"worlds": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение мира по идентификатору
        pk = идентификатор мира
        """
        queryset = World.objects.all()
        world = get_object_or_404(queryset, pk=pk)
        serializer = WorldSerializer(world)
        return Response(serializer.data)

class ThemeView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка тем
        """
        theme = Theme.objects.all()                
        serializer = ThemeListSerializer(theme, many=True)
        return Response({"themes": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение темы по идентификатору

        pk - идентификатор темы
        """
        queryset = Theme.objects.all()
        theme = get_object_or_404(queryset, pk=pk)
        serializer = ThemeSerializer(theme)        
        return Response(serializer.data)

class DeityView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка божеств
        """
        deity = Deity.objects.all()                
        serializer = DeitySerializer(deity, many=True)
        return Response({"deities": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение божеств по идентификатору

        pk - идентификатор божества
        """
        queryset = Deity.objects.all()
        deity = get_object_or_404(queryset, pk=pk)
        serializer = DeitySerializer(deity)        
        return Response(serializer.data)

class LanguageView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка языков
        """
        language = Language.objects.all()                
        serializer = LanguageSerializer(language, many=True)
        return Response({"Languages": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение языка по идентификатору

        pk - идентификатор языка
        """
        queryset = Language.objects.all()
        language = get_object_or_404(queryset, pk=pk)
        serializer = LanguageSerializer(language)        
        return Response(serializer.data)
        
class GameClassView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка классов
        """
        game_class = GameClass.objects.all()                
        serializer = GameClassListSerializer(game_class, many=True)
        return Response({"game_classes": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение класса по идентификатору

        pk - идентификатор класса
        """
        queryset = GameClass.objects.all()
        game_class = get_object_or_404(queryset, pk=pk)
        serializer = GameClassSerializer(game_class)        
        return Response(serializer.data)


class CharacterView(viewsets.ViewSet):
    def list(self, request):
        """Получение списка персонажей"""
        queryset = Character.objects.all()
        userCharacters = get_list_or_404(queryset, user=request.user)
        serializer = CharacterListSerializer(userCharacters, many=True)
        return Response({"characters": serializer.data})

    @action(detail=True, methods=['get'])
    def character_blank(self, request, pk=None):
        """
        Получение html страницы с листом персонажа

        pk - идентификатор персонажа
        """
        queryset = Character.objects.all()
        character = get_object_or_404(queryset, pk=pk)
        character_dto = CharacterManager(character).get_blank_dto()       

        return render(request, 'character/character_blank.html', {'character': character_dto})

    def retrieve(self, request, pk=None):
        """
        Получение персонажа по идентификатору

        pk - идентификатор персонажа
        """
        queryset = Character.objects.all()
        character = get_object_or_404(queryset, pk=pk)
        serializer = CharacterSerializer(character)        
        return Response(serializer.data)

    def post(self, request):
        """Создание персонажа"""
        name = request.data['name']
        if name is None:
            raise ValueError("Не задано имя")
        race_id = request.data['race_id']
        if race_id is None:
            raise ValueError("Не задана раса")            
        theme_id = request.data['theme_id']
        if theme_id is None:
            raise ValueError("Не задана тема")
        alignment_id = request.data['alignment_id']
        if alignment_id is None:
            raise ValueError("Не задано мировоззрение")
        deity_id = request.data['deity_id']
        world_id = request.data['world_id']
        subrace_id = request.data['subrace_id']
        class_id = request.data['class_id']
        if class_id is None:
            raise ValueError("Не задан класс")
        gender = request.data['gender']
        user = request.user
        builder = CharacterBuilder()
        character = builder.character(name, race_id, theme_id, alignment_id,
                     deity_id, class_id, gender, user, world_id, subrace_id)
        serializer = CharacterSerializer(character)        
        return Response(serializer.data)

    def put(self, request, pk=None):
        """Изменение персонажа"""
        queryset = Character.objects.all()
        character = get_object_or_404(queryset, pk=pk)
        serializer = CharacterSerializer(character, data=request.data) 
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """Удаление персонажа"""
        character = get_object_or_404(Character.objects.all(), pk=pk)
        character.delete()
        return Response({
            "message": "Персонаж с  id `{}` удален.".format(pk)
        }, status=204)

class FeatView(viewsets.ViewSet):
    def list(self, request):
        """Получение списка черт"""
        feats = Feat.objects.all()                
        serializer = FeatListSerializer(feats, many=True)
        return Response({"feats": serializer.data})

    def get_feats_by_character(self, request, character_id):
        """Получение списка черт доступны для выбора персонажем"""
        queryset = Character.objects.all()
        character = get_object_or_404(queryset, pk=character_id)
        feats = CharacterManager(character).get_feats_by_character() 
        serializer = FeatListSerializer(feats, many=True)
        return Response({"feats": serializer.data})