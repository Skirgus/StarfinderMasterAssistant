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
from .models import Theme, GameClass, Character
from .serializers import RaceSerializer, RaceDescriptionSerializer, RacePlayingForSerializer, RaceListSerializer
from .serializers import ThemeListSerializer, ThemeSerializer, GameClassListSerializer, GameClassSerializer, CharacterListSerializer

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