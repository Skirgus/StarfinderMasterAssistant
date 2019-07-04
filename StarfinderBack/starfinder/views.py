# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Race, RaceDescription, RacePlayingFor
from .models import Theme, GameClass, Character, Deity
from .serializers import RaceSerializer, RaceDescriptionSerializer, RacePlayingForSerializer, RaceListSerializer, DeitySerializer
from .serializers import ThemeListSerializer, ThemeSerializer, GameClassListSerializer, GameClassSerializer, CharacterListSerializer, CharacterSerializer

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

    def retrieve(self, request, pk=None):
        """
        Получение персонажа по идентификатору

        pk - идентификатор персонажа
        """
        queryset = Character.objects.all()
        character = get_object_or_404(queryset, pk=pk)
        serializer = CharacterSerializer(character)        
        return Response(serializer.data)

    def create_character(self, request):
        """Создание персонажа"""
        name = request.POST.get("name"),
        race_id = request.POST.get("race_id")
        theme_id = request.POST.get("theme_id")
        alignment_id = request.POST.get("alignment_id")
        deity_id = request.POST.get("deity_id")
        class_id = request.POST.get("class_id")
        gender = request.POST.get("gender")